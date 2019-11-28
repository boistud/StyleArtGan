from PIL import Image
import os
directories = []
class_names = []
for filename in os.listdir("subset_images2"):
	path = os.path.join("subset_images2",filename)
	#print(path)
	foo = Image.open(path)
	if foo.mode != 'RGB':
		foo = foo.convert('RGB')
	foo = foo.resize((512,512),Image.ANTIALIAS)

	new_path = "subset_images_resized"
	save_path = os.path.join(new_path,os.path.basename(path))
	foo.save(save_path,quality=95)
