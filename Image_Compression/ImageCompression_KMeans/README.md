# Image Compression using K-Means

This is a simple implentation of a K-Means algorithm used to compress a given .PNG image.

The code works in two stages. An encoding stage where the image is compressed to a simpler form and a decoding stage , where the image is reconstructed.

In the encoding stage , the K-Means algorithm is run to find n centroids. Each RGB pixel in the original image is replaced with a value in the range 0 - n. This reduces the size of the image to about one-third the original image. The compressed image is then stored as a 1-D array along with the n centroids and some other crucial information such as dimension of the original image which is required to reconstruct the image. All this information is stored into a file named "compressed.npz". This compressed file can be sent instead of original image and reconstructed on the recieving side. This marks the end of the encoding stage.

In the decoding stage, the image is simply reconstructed and reshaped into the original dimension. It can either be re-constructed as .PNG image or a .JPG. Conversion to .JPG is more beneficial as PIL module's JPG compression further reduces the size of the image on the receiving side. 


We have used a standard 512x512 image of Lenna with a size of 473.8 kB to test our compression. During the encoding stage, our "compressed.npz" had a size of 131.9 kB which outperformed several popular compression methods such as 

1. https://compressor.io which produced an image of 190 kB

2. http://compresspng.com/ which produced an image of 176.8 kB and few others.


### Original Image

<img src="https://github.com/PaiAkshay998/ImageCompression/blob/master/Lenna.png?raw=true" width="250px" height="250px">

### A visual representation of the data contained in "compressed.npz"

<img src="https://github.com/PaiAkshay998/ImageCompression/blob/master/Visual_representation_of_compressed_file.png?raw=true" width="250px" height="250px">


### Image After Reconstruction (in PNG)

<img src="https://github.com/PaiAkshay998/ImageCompression/blob/master/PNG_reconstruction.png?raw=true" width="250px" height="250px">


### Image After Reconstruction (in JPG)

<img src="https://github.com/PaiAkshay998/ImageCompression/blob/master/JPG_reconstruction.jpg?raw=true" width="250px" height="250px">

However , the compression is far from perfect since the encoding stage takes some time run the K-Means algorithm on the image for larger images or larger number of clusters.
