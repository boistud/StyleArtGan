import json
import os
import numpy as np
from shutil import copyfile

#metadata_to_idx = {'impressionism': 0, 'pop art': 1, 'portrait': 2, 'landscape': 3}

subset_dir = 'subset_images2/'

ip = 0
il = 0
Is = 0
ig = 0
cp = 0
cl = 0
cs = 0
cg = 0
ep = 0
el = 0
es = 0
eg = 0
sp = 0
sl = 0
ss = 0
sg = 0
hp = 0
hl = 0
hs = 0
hg = 0

max_number = 500

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
                                        
                                        labels.append([1,0,0,0,0,1,0,0,0])
                                        ip += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif il < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([1,0,0,0,0,0,1,0,0])
                                        il += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif Is < max_number and artwork['genre'] == 'sculpture':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([1,0,0,0,0,0,0,1,0])
                                        Is += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif ig < max_number and artwork['genre'] == 'genre painting':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([1,0,0,0,0,0,0,0,1])
                                        ig += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                elif artwork['style'] == 'Cubism' or artwork['style'] == 'Analytical Cubism':
                        
                        if cp < max_number and artwork['genre'] == 'portrait':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,1,0,0,0,1,0,0,0])
                                        cp += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif cl < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,1,0,0,0,0,1,0,0])
                                        cl += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif cs < max_number and artwork['genre'] == 'sculpture':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,1,0,0,0,0,0,1,0])
                                        cs += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif cg < max_number and artwork['genre'] == 'genre painting':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,1,0,0,0,0,0,0,1])
                                        cg += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                elif artwork['style'] == 'Expressionism' or artwork['style'] == 'Symbolism':
                        
                        if ep < max_number and artwork['genre'] == 'portrait':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,1,0,0,1,0,0,0])
                                        ep += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif el < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,1,0,0,0,1,0,0])
                                        el += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif es < max_number and artwork['genre'] == 'sculpture':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,1,0,0,0,0,1,0])
                                        es += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif eg < max_number and artwork['genre'] == 'genre painting':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,1,0,0,0,0,0,1])
                                        eg += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                elif artwork['style'] == 'Surrealism':
                        
                        if ep < max_number and artwork['genre'] == 'portrait':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,1,0,1,0,0,0])
                                        ep += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif el < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,1,0,0,1,0,0])
                                        el += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif es < max_number and artwork['genre'] == 'sculpture':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,1,0,0,0,1,0])
                                        es += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif eg < max_number and artwork['genre'] == 'genre painting':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,1,0,0,0,0,1])
                                        eg += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                elif artwork['style'] == 'High Renaissance':
                        
                        if hp < max_number and artwork['genre'] == 'portrait':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,0,1,1,0,0,0])
                                        hp += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                
                        elif hl < max_number and artwork['genre'] == 'landscape':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,0,1,0,1,0,0])
                                        hl += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif hs < max_number and artwork['genre'] == 'sculpture':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,0,1,0,0,1,0])
                                        hs += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')

                        elif hg < max_number and artwork['genre'] == 'genre painting':
                                
                                artist = artwork['artistUrl']
                                year = artwork['yearAsString']
                                artworkID = artwork['contentId']
                                
                                image_path = 'images/' + str(artist) + '/' + str(year) + '/' + str(artworkID) + '.jpg'
                                
                                if os.path.isfile(image_path):
                                        
                                        labels.append([0,0,0,0,1,0,0,0,1])
                                        hg += 1
                                        
                                        copyfile(image_path, subset_dir + str(artworkID) + '.jpg')
                                        
print(ip,il,Is,ig,cp,cl,cs,cg,ep,el,es,eg,hp,hl,hs,hg)
np.save(subset_dir + 'image.labels', np.array(labels))

