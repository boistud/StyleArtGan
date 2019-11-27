Learn more or give us feedback
from PIL import Image
import os
directories = []
class_names = []
for filename in os.listdir("datasets\\mydataset\\"):
	path = os.path.join("datasets\\mydataset\\",filename)
	print(path)
	foo = Image.open(path)
	foo = foo.resize((256,256),Image.ANTIALIAS)

	save_path = path.split("\\")[-1]
	foo.save(save_path,quality=95)
