# Neural Style Transfer
This project is a TensorFlow implementation of A Neural Algorithm of Artistic Style by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge, which implement a VGG-19 network perform image style transfer.

## Prerequisites
- Python 3.3 or above
- [Pytorch 0.4.0](torch.org)

Install package 'imageio' and ‘scipy’ as follow:

```
$ pip install --user imageio
$ pip install --user scipy
```

## Dataset
We download several images as content and style back plate. All these images are used in **[Gatys' paper](https://arxiv.org/pdf/1508.06576.pdf)** so that we can implement the style transfer effect as more as possible.
More style images can be download from WikiArt(https://www.wikiart.org/en/vincent-van-gogh)

## VGG-19
We use a pre-trained VGG network, with the network weights being stored in imagenet-vgg-verydeep-19.mat, which can be downloaded from https://drive.google.com/file/d/18sGBLRR_whhRUW0Tf3PXs3z6EOmYmiMW/view. This is a large file, and along with vggnet.py, it acts as a proxy for the CNN model.

## Code organization
The project code is in the `styleTransfer` folder and organized as follows:

Style_transfer_demo.ipynb    --  Main code for loading images, running and training model, and generating new artictic style image. 

utils.py  --  Function load_image and save_image to load and save images.

loss.py   --  Functions to calculate content loss and style loss.

train.py  --  Contains VGG class the defines the VGG-19 configuration

Code in `optimizer` and `reconstruct` is used to show how the style transfer implemented by reconstructing content and style image after particular convolution layers. 

## Result
All corresponding results is saved in `styleTransfer/images/result`
Each result image is named by its style and content followed by its corresponding iteration times.

## Demo
Please visit the demo website to see more results!

**[Demo Website](https://sites.google.com/view/ece285-styletransfer/%E9%A6%96%E9%A1%B5?authuser=1)**

## Reference
[1] L. Gatys, A. Ecker, and M. Bethge, “A neural algorithm of artistic style,” Journal of Vision, vol. 16, no. 12, p. 326, 2016.

[2] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image recognition,” in International Conference on Learning Representations, 2015.

[3] R. Novak and Y. Nikulin, “Improving the neural algorithm of artistic style,” CoRR, vol. abs/1605.04603, 2016.

