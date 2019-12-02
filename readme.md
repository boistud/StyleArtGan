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
| [StyleGAN](http://stylegan.xyz/drive) | Main folder.
| &boxvr;&nbsp; [stylegan-paper.pdf](https://drive.google.com/open?id=1v-HkF3Ehrpon7wVIx4r5DLcko_U_V6Lt) | High-quality version of the paper PDF.
| &boxvr;&nbsp; [stylegan-video.mp4](https://drive.google.com/open?id=1uzwkZHQX_9pYg1i0d1Nbe3D9xPO8-qBf) | High-quality version of the result video.
| &boxvr;&nbsp; [images](https://drive.google.com/open?id=1-l46akONUWF6LCpDoeq63H53rD7MeiTd) | Example images produced using our generator.
| &boxv;&nbsp; &boxvr;&nbsp; [representative-images](https://drive.google.com/open?id=1ToY5P4Vvf5_c3TyUizQ8fckFFoFtBvD8) | High-quality images to be used in articles, blog posts, etc.


# Datasets for Training

A random sample of images for specific styles and genres used training was converted to tfrecords along with the labels.npy which contains class labels (styles and genres of each image).

* Styles: Impressionisn, Cubism (Analytical Cubism), Expressionism (Symbolism), Surrealism, High Renaissance
* Genres: Portrait, Landscape, Sculpture, Genre Painting

# Evaluations



# Results

Painting: Generated Grid for each style
![Grid](https://github.com/boistud/StyleArtGan/blob/master/Results/grid_edited.png)

Painting: Generated style mixing
![Style Mixing](https://github.com/boistud/StyleArtGan/blob/master/Results/mixing_edited.png)

