# Style Art Gan

This git page is devoted to walk you through how our team, motivated by the original StyleGan paper, attempted to generated realistic paintings by modifying the original StyleGan architecture to incorporate class labels namely different styles and genres of paintings to be able to get more stable results and to have more control over the generated images.


# Resources

The dataset is obtained from the Wiki-Art https://www.wikiart.org/ containing art work based on styles, genres, and media. 

# System Requirements

* At least one NVIDIA GPU with at least 11GB of DRAM. We trained our model with one p100 GPU provided by the Google Cloud Platform
* Python 3.6 installation 
* TensorFlow-gpu 1.11.0 
* CUDA toolkit corresponding the Tensorflow-gpu

# Files



# Datasets for Training

The paintings are converted to latent space using TF-Records. 

# Evaluations



# Results

Painting: Generated Grid for each style
![Grid](https://github.com/boistud/StyleArtGan/blob/master/Results/grid_edited.png)

Painting: Generated style mixing
![Style Mixing](https://github.com/boistud/StyleArtGan/blob/master/Results/mixing_edited.png)

