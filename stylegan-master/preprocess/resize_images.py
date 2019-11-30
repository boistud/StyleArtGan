from PIL import Image
import os

class Converter:
	def __init__(self, image_resolution, file):
		self.image_resolution = image_resolution # e.g. (512,512)
		self.file = file
		
	def convert():
		for filename in os.listdir(file):
			path = os.path.join(file,filename)
			
			foo = Image.open(path)
			if foo.mode != 'RGB':
				foo = foo.convert('RGB')
			foo = foo.resize(self.image_resolution,Image.ANTIALIAS)

			new_path = "subset_images_resized"
			save_path = os.path.join(new_path,os.path.basename(path))
			foo.save(save_path,quality=95)
