import generate_figures as gf
import os
import config
import pickle
from io import BytesIO
import dnnlib
import numpy as np
import PIL.Image
import dnnlib.tflib as tflib

# generates image(s) with every style in styles and every genre in genres and outputs them to the output file
# if generating multiple images, they are concatenated into one large image
def generate_image(pickle_file, styles, genres, output_file, n_images=1):

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
	rnd = np.random.RandomState(5)
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

# generates images for every style/genre combo and saves them all as one tiled image where each row is a style and each column is a genre
def generate_image_grid(pickle_file, output_file, styles=None, genres=None):

	tflib.init_tf()

	# must be a perfect square
	images_per_combo = 4

	# an ordered list of the styles to put into the grid
	all_styles = ['impressionism', 'cubism', 'analytical cubism', 'expressionism', 'symbolism', 'surrealism', 'high renaissance']
	all_genres = ['portrait', 'landscape', 'sculpture', 'genre painting']

	styles_to_idx = {'impressionism': 0, 'cubism': 1, 'analytical cubism': 1, 'expressionism': 2, 'symbolism': 2, 'surrealism': 3, 'high renaissance': 4}
	genres_to_idx = {'portrait': 5, 'landscape': 6, 'sculpture': 7, 'genre painting': 8}

	max_index = 8

	f = open(pickle_file,"rb")
	bin_data = f.read()
	sio = BytesIO(bin_data)
	_G, _D, Gs = pickle.load(sio)

	# generate the random input vectors
	rnd = np.random.RandomState(5)
	latents = rnd.randn(images_per_combo, Gs.input_shape[1])

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

	# this will be the final image
	grid = None

	for style in all_styles:

		# this will be all the images for this style concatenated together
		row = None

		for genre in all_genres:

			# initialize the label
			label = [0] * (max_index + 1)

			# set the label
			label[styles_to_idx[style.lower()]] = 1
			label[genres_to_idx[genre.lower()]] = 1

			# duplicate the label as needed
			labels = [label] * images_per_combo

			# generate the images
			images = Gs.run(latents, labels, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

			# format the grid and the images in it
			side_length = np.sqrt(images_per_combo)

			# make the first row of this output
			output = np.concatenate((images[:side_length]), axis=1)

			# concatenate the rest of the rows
			for i in range(1, side_length):

				output = np.concatenate((output, np.concatenate((images[i * side_length: (i + 1) * side_length]), axis=1)), axis=0)

			# add this output to the row
			if row is None:

				row = output.copy()

			else:

				row = np.concatenate((row, output), axis=1)

		# add this row to the grid
		if grid is None:

			grid = row.copy()

		else:

			grid = np.concatenate((grid, row), axis=0)

	# save the image
	PIL.Image.fromarray(grid, 'RGB').save(output_file)

generate_image_grid('results/00015-sgan-sampleset-cond-1gpu-tuned-baseline-add-mapping-and-styles-remove-traditional-input-add-noise-inputs-stylebased-2/network-snapshot-006126.pkl', output_file='grid.png')