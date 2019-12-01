import generate_figures as gf
import os
import config
import pickle
from io import BytesIO
import dnnlib
import numpy as np
#import matplotlib.pyplot as plt
import PIL.Image
import dnnlib.tflib as tflib

tflib.init_tf()

dir = 'results/00015-sgan-sampleset-cond-1gpu-tuned-baseline-add-mapping-and-styles-remove-traditional-input-add-noise-inputs-stylebased-2/network-snapshot-006126.pkl'

f = open(dir,"rb")
bin_data = f.read()
sio = BytesIO(bin_data)
_G, _D, Gs = pickle.load(sio)

#gf.draw_style_mixing_figure(os.path.join(config.result_dir, 'figure03-style-mixing.png'), Gs, w=512, h=512, src_seeds=[639,701,687,615,2268], dst_seeds=[888,829,1898,1733,1614,845], style_ranges=[range(0,4)]*3+[range(4,8)]*2+[range(8,18)])

rnd = np.random.RandomState(5)
#print(Gs.input_shape)
latents = rnd.randn(8, Gs.input_shape[1])
#latents[:,0] = np.array([1,0,1,0])
#latents[0][-4:] = np.array([1,0,1,0])
labels = np.array([[1,0,0,0,0,0,1,0,0]] * 8)
#labels = np.transpose(labels)

# Generate image.

fmt = dict(func=dnnlib.tflib.convert_images_to_uint8, nchw_to_nhwc=True)
images = Gs.run(latents, labels, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

output = np.concatenate(([img for img in images]), axis=1)

#os.makedirs(config.result_dir, exist_ok=True)c
png_filename = 'take1.png'
PIL.Image.fromarray(output, 'RGB').save(png_filename)
