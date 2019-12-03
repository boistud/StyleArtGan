# The directories only exist on the VM since images are too big to push on git
# Convert images to tfrecords and add labels(style+genre) as well
import dataset_tool as dt
import preprocess


# resize images and then save them
corvett = resize_images.Converter(image_resolution=(512,512),file='subset_images2')
corvett.convert()

# load images from the saved folder and convert to tfrecords
dt.create_from_images('datasets//subset_images_tfr', '..//..//wikiart-master//wikiart-saved//subset_images_resized', True)
