"""
Created on Sat Nov  9 20:10:06 2019
@author: joshu
"""

import json
import os
import numpy as np
from shutil import copyfile

metadata_to_idx = {'impressionism': 0, 'pop art': 1, 'portrait': 2, 'landscape': 3}

image_dir = 'images/'

labels = []

for filename in os.listdir('./meta'):
        
        with open('meta/' + filename, encoding='utf8') as json_file:
                
                parsed_json = json.load(json_file)
                
                json_file.close()
        
        for artwork in parsed_json:

                label = [0] * len(metadata_to_idx)

                if artwork['style'] in metadata_to_idx:

                        label[metadata_to_idx[artwork['style']]] = 1

                if artwork['genre'] in metadata_to_idx:

                        label[metadata_to_idx[artwork['style']]] = 1

                labels.append(label)
                                        
np.save(subset_dir + 'prelim.labels', np.array(labels))
