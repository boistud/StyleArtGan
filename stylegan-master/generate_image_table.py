import generate_figures as gf
import os
import config
import pickle
from io import BytesIO
import dnnlib
import numpy as np
import PIL.Image
import dnnlib.tflib as tflib
import math
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# generates image(s) with every style in styles and every genre in genres and outputs them to the output file
# if generating multiple images, they are concatenated into one large image
def generate_image(pickle_file, styles, genres, output_file, n_images=1, seed=None):

	tflib.init_tf()

	# map the features to their label indices
	styles_to_idx = {'impressionism': 0, 'cubism': 1, 'analytical cubism': 1, 'expressionism': 2, 'symbolism': 2, 'surrealism': 3, 'high renaissance': 4}
	genres_to_idx = {'portrait': 5, 'landscape': 6, 'sculpture': 7, 'genre painting': 8}

	max_index = 8

	# load the model
	f = open(pickle_file,"rb")
	bin_data = f.read()
	sio = BytesIO(bin_data)
	_G, _D, Gs = pickle.load(sio)

	# generate the random input vectors
	rnd = np.random.RandomState(seed)
	latents = rnd.randn(n_images, Gs.input_shape[1])

	# initialize the label vector
	label = [0] * (max_index + 1)

	# for each style
	for style in styles:

		# check that it is a valid style
		if style.lower() not in styles_to_idx:

			print('Error: \'' + str(style) + '\' not a valid style.')

			return

		# update the label
		label[styles_to_idx[style.lower()]] = 1

	# do the same for each genre
	for genre in genres:

		if genre.lower() not in genres_to_idx:

			print('Error: \'' + str(genre) + '\' not a valid genre.')

			return

		label[styles_to_idx[genre.lower()]] = 1

	# duplicate the label as many times as it is needed
	labels = np.array([label] * n_images)

	# Generate the images
	fmt = dict(func=dnnlib.tflib.convert_images_to_uint8, nchw_to_nhwc=True)
	images = Gs.run(latents, labels, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

	# make sure the output is just one image
	if n_images > 1:

		output = np.concatenate(([img for img in images]), axis=1)

	else:

		output = images[0]

	# save the image to file
	PIL.Image.fromarray(output, 'RGB').save(output_file)

# generates images with style mixing from specified artistic styles and genres
def generate_style_mix(pickle_file, fine_style, fine_genre, coarse_style, coarse_genre, output_file, n_images=1, seed=100):

	tflib.init_tf()

	# dictionaries for building the labels
	styles_to_idx = {'impressionism': 0, 'cubism': 1, 'analytical cubism': 1, 'expressionism': 2, 'symbolism': 2, 'surrealism': 3, 'high renaissance': 4}
	genres_to_idx = {'portrait': 5, 'landscape': 6, 'sculpture': 7, 'genre painting': 8}

	# the max index in the dictionaries
	max_index = 8

	# load the model
	f = open(pickle_file,"rb")
	bin_data = f.read()
	sio = BytesIO(bin_data)
	_G, _D, Gs = pickle.load(sio)

	# generate the random input vectors
	rnd = np.random.RandomState(seed)
	fine_latents = rnd.randn(n_images, Gs.input_shape[1])
	rnd = np.random.RandomState(seed * 2)
	coarse_latents = rnd.randn(n_images, Gs.input_shape[1])

	# initialize the labels
	fine_label = [0] * (max_index + 1)
	coarse_label = [0] * (max_index + 1)

	# check that the specified styles and genres are valid
	if fine_style.lower() not in styles_to_idx:

		print('Error: \'' + str(fine_style) + '\' not a valid style')

		return

	if fine_genre.lower() not in genres_to_idx:

		print('Error: \'' + str(fine_genre) + '\' not a valid genre')

		return

	if coarse_style.lower() not in styles_to_idx:

		print('Error: \'' + str(coarse_style) + '\' not a valid style')

		return

	if coarse_genre.lower() not in genres_to_idx:

		print('Error: \'' + str(coarse_genre) + '\' not a valid genre')

		return

	# set the labels
	fine_label[styles_to_idx[fine_style.lower()]] = 1
	fine_label[genres_to_idx[fine_genre.lower()]] = 1
	coarse_label[styles_to_idx[coarse_style.lower()]] = 1
	coarse_label[genres_to_idx[coarse_genre.lower()]] = 1

	# duplicate the labels as needed
	fine_labels = [fine_label] * n_images
	coarse_labels = [coarse_label] * n_images

	# pass the labels and latents through the mapping network
	fine_dlatents = Gs.components.mapping.run(fine_latents, fine_labels)
	coarse_dlatents = Gs.components.mapping.run(coarse_latents, coarse_labels)

	fmt = dict(func=dnnlib.tflib.convert_images_to_uint8, nchw_to_nhwc=True)

	# generate the images whose styles are to be mixed
	fine_images = Gs.components.synthesis.run(fine_dlatents, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)
	coarse_images = Gs.components.synthesis.run(coarse_dlatents, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

	# initialize the mixed dlatents list
	mixed_dlatents = []

	# for each pair of images
	for i in range(len(fine_images)):

		# take the fine dlatents
		mixed_dlatents.append(fine_dlatents[i].copy())

		# and copy the coarse dlatents over the second half
		mixed_dlatents[i][0][int(len(mixed_dlatents[i][0]) / 2):] = coarse_dlatents[i][0][int(len(mixed_dlatents[i][0]) / 2):]

	# generate the style-mixed images
	mixed_images = Gs.components.synthesis.run(np.array(mixed_dlatents), truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

	# concatenate the images into a nice figure
	figure = np.concatenate(([np.concatenate((coarse_images), axis=1), np.concatenate((mixed_images), axis=1), np.concatenate((fine_images), axis=1)]), axis=0)

	# save the figure
	PIL.Image.fromarray(figure, 'RGB').save(output_file)

# generates images for every style/genre combo and saves them all as one tiled image where each row is a style and each column is a genre
def generate_image_grid(pickle_file, output_file, styles=None, genres=None, seed=100):

	tflib.init_tf()

	# must be a perfect square
	images_per_combo = 4

	# for formatting the grid and the images in it
	side_length = int(math.sqrt(images_per_combo))

	# an ordered list of the styles to put into the grid
	all_styles = ['impressionism', 'cubism', 'expressionism', 'surrealism', 'high renaissance']
	all_genres = ['portrait', 'landscape', 'sculpture', 'genre painting']

	styles_to_idx = {'impressionism': 0, 'cubism': 1, 'analytical cubism': 1, 'expressionism': 2, 'symbolism': 2, 'surrealism': 3, 'high renaissance': 4}
	genres_to_idx = {'portrait': 5, 'landscape': 6, 'sculpture': 7, 'genre painting': 8}

	max_index = 8

	f = open(pickle_file,"rb")
	bin_data = f.read()
	sio = BytesIO(bin_data)
	_G, _D, Gs = pickle.load(sio)

	fmt = dict(func=dnnlib.tflib.convert_images_to_uint8, nchw_to_nhwc=True)

	# check that any specified styles are valid
	if styles != None:

		for style in styles:

			if style.lower() not in styles_to_idx:

				print('Error: \'' + str(style) + '\' not a valid style.')

				return

		all_styles = styles

	# check any specified genres too
	if genres != None:

		for genre in genres:

			if genre.lower() not in genres_to_idx:

				print('Error: \'' + str(genre) + '\' not a valid genre.')

				return

		all_genres = genres

	#f, axarr = plt.subplots(len(all_styles), len(all_genres))

	# this will be the final image
	grid = None

	row_number = 0

	k = 1

	for style in all_styles:

		# this will be all the images for this style concatenated together
		row = None

		column_number = 0

		for genre in all_genres:

			# initialize the label
			label = [0] * (max_index + 1)

			# set the label
			label[styles_to_idx[style.lower()]] = 1
			label[genres_to_idx[genre.lower()]] = 1

			# duplicate the label as needed
			labels = [label] * images_per_combo

			# generate the random input vectors
			rnd = np.random.RandomState(seed * k)
			latents = rnd.randn(images_per_combo, Gs.input_shape[1])

			k += 1

			# generate the images
			images = Gs.run(latents, labels, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

			# make the first row of this output
			output = np.concatenate((images[:side_length]), axis=1)

			# concatenate the rest of the rows
			for i in range(1, side_length):

				output = np.concatenate((output, np.concatenate((images[i * side_length: (i + 1) * side_length]), axis=1)), axis=0)

			#axarr[row_number, column_number].imshow(output)

			#axarr[row_number, column_number].axis('off')

			# add this output to the row
			if row is None:

				row = output.copy()

			else:

				row = np.concatenate((row, output), axis=1)

			column_number += 1

		# add this row to the grid
		if grid is None:

			grid = row.copy()

		else:

			grid = np.concatenate((grid, row), axis=0)

		row_number += 1

	#for i in range(len(all_styles)):

		#axarr[i,0].set_ylabel(all_styles[i])

	#for i in range(len(all_genres)):

		#axarr[0,i].set_title(all_genres[i])

	#f.tight_layout()
	#plt.savefig(output_file, bbox_inches='tight', pad_inches=0)

	# save the image
	PIL.Image.fromarray(grid, 'RGB').save(output_file)

#generate_image_grid('results/00015-sgan-sampleset-cond-1gpu-tuned-baseline-add-mapping-and-styles-remove-traditional-input-add-noise-inputs-stylebased-2/network-snapshot-006126.pkl', output_file='grid.png', genres=['portrait', 'landscape'], seed=5)

generate_style_mix('results/00015-sgan-sampleset-cond-1gpu-tuned-baseline-add-mapping-and-styles-remove-traditional-input-add-noise-inputs-stylebased-2/network-snapshot-006126.pkl', fine_style='cubism', fine_genre='portrait', coarse_style='impressionism', coarse_genre='landscape', output_file='mixing.png', n_images=8, seed=6)