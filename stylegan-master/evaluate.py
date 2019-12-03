import metrics
import dnnlib
import os
import config
import pickle
from io import BytesIO
import dnnlib.tflib as tflib
from easydict import EasyDict
import config
from metrics import metric_base
from metrics import frechet_inception_distance as fid
from training import misc
from training import dataset

# Evaluate a network by FID score

# Directory of the pickled model saved under the folder 'results'

def evaluate(dir):
  
  tflib.init_tf()

  f = open(dir + 'network-final.pkl',"rb")
  bin_data = f.read()
  sio = BytesIO(bin_data)
  _G, _D, Gs = pickle.load(sio)

  #fid = dnnlib.EasyDict(func_name='metrics.frechet_inception_distance.FID', name='fid50k', num_images=2788, minibatch_per_gpu=8)

  #dataset = EasyDict(tfrecord_dir='subset_images_tfr')

  evaluater = fid.FID(num_images=2788, minibatch_per_gpu=8, name='fid')
  #run_config = misc.parse_config_for_previous_run(dir)
  #print(run_config)
  #evaluater.run = dict(run_config['dataset'])
  evaluater.run(dir + 'network-final.pkl', run_dir=dir, dataset_args=None, mirror_augment=True, num_gpus=1)
  evaluater._evaluate(Gs, 1)

dir = 'results/00005-sgan-sampleset-cond-1gpu-tuned-baseline-add-mapping-and-styles-remove-traditional-input-add-noise-inputs-stylebased-2/'
evaluate(dir)
