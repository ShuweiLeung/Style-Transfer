import imageio
import scipy.misc
import numpy as np
from PIL import Image


'''
parser.add_argument("--content",
                    help="Enter the content image",
                    dest="content_image",
                    type=str,
                    default="./images/content/tuebingen_neckarfront.jpg")

parser.add_argument("--style",
                    help="Enter the style image",
                    dest="style_image",
                    type=str,
                    default=".images/style/starry-night-van-gogh.jpg")
parser.add_argument("--output",
                    help="Enter the output directory",
                    dest="output_directory",
                    type=str,
                    default=".images/result")

parser.add_argument("--width",
                    help="Enter the image width",
                    dest="image_width",
                    type=int,
                    default=800)

parser.add_argument("--height",
                    help="Enter the image height",
                    dest="image_height",
                    type=int,
                    default=600)

parser.add_argument("--alpha",
                    help="Enter the weight factor for content",
                    dest="alpha",
                    type=int,
                    default=10)

parser.add_argument("--beta",
                    help="Enter the weight factor for style",
                    dest="beta",
                    type=int,
                    default=1000)

parser.add_argument("--vgg",
                    help="Enter the VGG19 model",
                    dest="vgg",
                    type=str,
                    default="imagenet-vgg-verydeep-19.mat")

parser.add_argument("--iterations",
                    help="Enter the number of iterations",
                    dest="iterations",
                    type=int,
                    default=1000)

arguments = parser.parse_args()
image_height = arguments.image_height
image_width = arguments.image_width

'''



# Function to resize input image and store it as an array
def initialize_image(path):
    image = scipy.misc.imread(path)
    #image = scipy.misc.imresize(image, (image_height, image_width))
    image = scipy.misc.imresize(image, (600, 800))
    image = image[np.newaxis, :, :, :]
    return image


# Function to save the output image at each interval
def save_image(path, image):
    scipy.misc.imsave(path, image[0])
    

# the BGR means from the ImageNet database
IMAGENET_MEANS = np.array([103.939, 116.779, 123.68])


def load_image(image_path: str, size: tuple=None) -> Image:
    """
    Load and return an image at a given path.

    Args:
        image_path: the path of the image to load
        size: a tuple of (width, height) to resize the image (default None)

    Returns:
        the image loaded from the given path

    """
    # load the image from the path
    image = Image.open(image_path)
    # if a size is provided
    if size is not None:
        # apply the size to the image
        image = image.resize(size)

    return image
