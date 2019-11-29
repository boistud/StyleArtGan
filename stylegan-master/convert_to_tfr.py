# The directories only exist on the VM since images are too big to push on git

import dataset_tool as dt

dt.create_from_images('..//..//wikiart-master/wikiart-saved/subset_images_tfr//', '..//..//wikiart-master//wikiart-saved//subset_images_resized', True)
