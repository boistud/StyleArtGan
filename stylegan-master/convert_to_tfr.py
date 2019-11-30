# The directories only exist on the VM since images are too big to push on git
# Convert images to tfrecords and add labels(style+genre) as well
import dataset_tool as dt

dt.create_from_images('..//..//StyleArtGan-master//stylegan-master//datasets//', '..//..//wikiart-master//wikiart-saved//subset_images_resized', True)

