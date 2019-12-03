# Style Art Gan

This git page is devoted to walk you through how our team, motivated by the original StyleGan paper, attempted to generated realistic paintings by modifying the original StyleGan architecture to incorporate class labels namely different styles and genres of paintings to be able to get more stable results and to have more control over the generated images.


# Resources

The dataset is obtained from the Wiki-Art https://www.wikiart.org/ containing art work based on styles, genres, and texture. 

# System Requirements

* At least one NVIDIA GPU with at least 11GB of DRAM. We trained our model with one p100 GPU provided by the Google Cloud Platform
* Python 3.6 installation 
* TensorFlow-gpu 1.9.0 
* CUDA 9.0 installation
* CUDA toolkit corresponding the Tensorflow-gpu

# Files
| Path | Description
| :--- | :----------
| [Results](https://github.com/boistud/StyleArtGan/tree/master/Results)| Contains the final report and some of the images used in the paper.
| [stylegan-master](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master)| primary directory
| &boxvr;&nbsp; [Datasets](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master/datasets) | dataset path pointed by train.py
| &boxv;&nbsp; &boxur;&nbsp;[subset_images_tfr](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master/datasets/subset_images_tfr) | folder where tfrecords are stored
| &boxv;&nbsp; &ensp;&ensp; &boxur;&nbsp;[placeholder.txt](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master/datasets/subset_images_tfr/placeholder.txt) | placeholder since the actual tfrecords are too big
| &boxv;&nbsp; [dnnlib](https://github.com/alex91121/Style_Art_GAN/tree/master/stylegan-master-clean/dnnlib) | helper functions
| &boxv;&nbsp; [metrics](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master/metrics) | various metric functions
| &boxv;&nbsp; [preprocess](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master/preprocess) | preprocess functions
| &boxvr;&nbsp; &boxvr;&nbsp; [collect_images.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/preprocess/collect_images.py) | collect images from wikiart dataset folder
| &boxvr;&nbsp; &boxur;&nbsp; [resize_images.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/preprocess/resize_images.py) | resize collected images so that they are compatible with the model architecture
| &boxv;&nbsp; [training](https://github.com/boistud/StyleArtGan/tree/master/stylegan-master/training) | folder that contains actual networks and training process
| &boxv;&nbsp [config.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/config.py) | global configuration
| &boxv;&nbsp [convert_to_tfr.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/convert_to_tfr.py) | convert resized iamges to tfrecords
| &boxv;&nbsp [dataset_tool.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/dataset_tool.py) | helper functions for dealing with datasets
| &boxv;&nbsp [evaluate.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/evaluate.py) | evaluate models by loading saved .pkl model and computing FID score
| &boxv;&nbsp [generate_figures.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/generate_figures.py) | various functions for generating figures of different sorts
| &boxv;&nbsp [generate_image_table.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/generate_image_table.py) | generate style mixing and grid images by loading the saved .pkl model
| &boxv;&nbsp [run_metrics.py](https://github.com/boistud/StyleArtGan/blob/master/stylegan-master/run_metrics.py) | helper functions for loading saved models
| [readme.md](https://github.com/boistud/StyleArtGan/blob/master/readme.md)| readme file


# Datasets for Training

A random sample of images for specific styles and genres used training was converted to tfrecords along with the labels.npy which contains class labels (styles and genres of each image).

* Styles: Impressionisn, Cubism (Analytical Cubism), Expressionism (Symbolism), Surrealism, High Renaissance
* Genres: Portrait, Landscape, Sculpture, Genre Painting

# Evaluations



# Results

* Painting: Generated Grid for each style
![Grid](https://github.com/boistud/StyleArtGan/blob/master/Results/grid_edited.png)

* Painting: Generated style mixing
![Style Mixing](https://github.com/boistud/StyleArtGan/blob/master/Results/mixing_edited.png)

