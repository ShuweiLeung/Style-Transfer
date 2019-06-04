# Style Transfer

**Team: MLYZ**

**Members\: Qi Ma, Shuwei Liang, Zhuo Yue, Cong Zhao**

## Neural Style Transfer
**We implemented the algorithm in Gatys paper on "A Neural Algorithm for Artistic Style". The artifical system is based on deep neural network, it uses neural representations to separate and recombine content and style images. We applied 16 convolutional and 5 average pooling layers of the VGG-19 network. 
**We perform a white noise image to find another image that matches the feature responses of the originnal image. Then define squared-error loss between two feature represenntations as content-loss. 
**The feature correlations are given by Gram matrix, so we also generate the Gram matrix between the vectorized feature maps i and j in layer l.
**To generate a texture that matches the style of a given style image, we use gradient decent (in fact, we use L_BFGS as achievement of lower loss) from a white noise image to find anotherimage that matches the style representations of the original image, which is done by minimizing the mean-squared distance between the entries of the Gram matrix from the original image and the Gram matrix of the image to be generated. 
**The total loss is weighted sum of content-loss and style-loss. We then have to determine the ratio of weights of content-loss and tyle-loss in training.

## Image-to-Image Translation using Cycle-GANs
