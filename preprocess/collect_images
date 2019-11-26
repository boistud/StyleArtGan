import json
import os
import numpy as np
from shutil import copyfile

#metadata_to_idx = {'impressionism': 0, 'pop art': 1, 'portrait': 2, 'landscape': 3}

subset_dir = 'subset_images2/'

ip = 0
il = 0
pap = 0
pal = 0

max_number = 100

labels = []

for filename in os.listdir('./meta'):
        
        with open('meta/' + filename, encoding='utf8') as json_file:
                
                parsed_json = json.load(json_file)
                
                json_file.close()
        
        for artwork in parsed_json:
                
                if artwork['style'] == 'Impressionism':
                        
                        if ip < max_number and artwork['genre'] == 'portrait':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([1,0,1,0])
                                        ip += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif il < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([1,0,0,1])
                                        il += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                elif artwork['style'] == 'Cubism':
                        
                        if pap < max_number and artwork['genre'] == 'portrait':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,1,1,0])
                                        pap += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif pal < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,1,0,1])
                                        pal += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                        
print(ip, il, pap, pal)
np.save(subset_dir + 'prelim.labels', np.array(labels))
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
