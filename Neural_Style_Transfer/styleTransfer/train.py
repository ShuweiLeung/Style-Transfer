import tensorflow as tf 
import scipy.io
import numpy as np


# Function for convolution using weights
def convolution(prev_layer, weights):
    return tf.nn.conv2d(prev_layer, weights, strides=(1, 1, 1, 1), padding="SAME")


# Function for relu using bias
def relu(prev_layer, bias):
    return tf.nn.relu(prev_layer + bias)

# Function to apply average pooling as suggested in the paper
def avg_pool(prev_layer):
    return tf.nn.avg_pool(prev_layer, ksize=(1, 2, 2, 1), strides=(1, 2, 2, 1), padding="SAME")


# Funtion to get weights to be used for convolution
def get_weights(layer, i):
    weights = layer[i][0][0][0][0][0]
    weights = tf.constant(weights)
    return weights


# Funtion to get bias to be used for relu activation
def get_bias(layer, i):
    bias = layer[i][0][0][0][0][1]
    bias = tf.constant(bias)
    return bias


# Create vgg19 network
def vgg19(datapath):
    net = {}
    vgg_mat = scipy.io.loadmat(datapath)
    vgg_layers = vgg_mat["layers"][0]
    
    net["input"] = tf.Variable(np.zeros((1, 600, 800, 3),
                                          dtype=np.float32))
    
    # Block 1
    net["conv1_1"] = convolution(net["input"], get_weights(vgg_layers, 0))
    net["relu1_1"] = relu(net["conv1_1"], get_bias(vgg_layers, 2))
    net["conv1_2"] = convolution(net["relu1_1"], get_weights(vgg_layers, 2))
    net["relu1_2"] = relu(net["conv1_2"], get_bias(vgg_layers, 2))
    net["avg_pool1"] = avg_pool(net["relu1_2"])
    
    # Block 2
    net["conv2_1"] = convolution(net["avg_pool1"], get_weights(vgg_layers, 5))
    net["relu2_1"] = relu(net["conv2_1"], get_bias(vgg_layers, 5))
    net["conv2_2"] = convolution(net["relu2_1"], get_weights(vgg_layers, 7))
    net["relu2_2"] = relu(net["conv2_2"], get_bias(vgg_layers, 7))
    net["avg_pool2"] = avg_pool(net["relu2_2"])
    
    # Block 3
    net["conv3_1"] = convolution(net["avg_pool2"], get_weights(vgg_layers, 10))
    net["relu3_1"] = relu(net["conv3_1"], get_bias(vgg_layers, 10))
    net["conv3_2"] = convolution(net["relu3_1"], get_weights(vgg_layers, 12))
    net["relu3_2"] = relu(net["conv3_2"], get_bias(vgg_layers, 12))
    net["conv3_3"] = convolution(net["relu3_2"], get_weights(vgg_layers, 14))
    net["relu3_3"] = relu(net["conv3_3"], get_bias(vgg_layers, 14))
    net["conv3_4"] = convolution(net["relu3_3"], get_weights(vgg_layers, 16))
    net["relu3_4"] = relu(net["conv3_4"], get_bias(vgg_layers, 16))
    net["avg_pool3"] = avg_pool(net["relu3_4"])
    
    # Block 4
    net["conv4_1"] = convolution(net["avg_pool3"], get_weights(vgg_layers, 19))
    net["relu4_1"] = relu(net["conv4_1"], get_bias(vgg_layers, 19))
    net["conv4_2"] = convolution(net["relu4_1"], get_weights(vgg_layers, 21))
    net["relu4_2"] = relu(net["conv4_2"], get_bias(vgg_layers, 21))
    net["conv4_3"] = convolution(net["relu4_2"], get_weights(vgg_layers, 23))
    net["relu4_3"] = relu(net["conv4_3"], get_bias(vgg_layers, 23))
    net["conv4_4"] = convolution(net["relu4_3"], get_weights(vgg_layers, 25))
    net["relu4_4"] = relu(net["conv4_4"], get_bias(vgg_layers, 25))
    net["avg_pool4"] = avg_pool(net["relu4_4"])
    
    # Block 5
    net["conv5_1"] = convolution(net["avg_pool4"], get_weights(vgg_layers, 28))
    net["relu5_1"] = relu(net["conv5_1"], get_bias(vgg_layers, 28))
    net["conv5_2"] = convolution(net["relu5_1"], get_weights(vgg_layers, 30))
    net["relu5_2"] = relu(net["conv5_2"], get_bias(vgg_layers, 30))
    net["conv5_3"] = convolution(net["relu5_2"], get_weights(vgg_layers, 32))
    net["relu5_3"] = relu(net["conv5_3"], get_bias(vgg_layers, 32))
    net["conv5_4"] = convolution(net["relu5_3"], get_weights(vgg_layers, 34))
    net["relu5_4"] = relu(net["conv5_4"], get_bias(vgg_layers, 34))
    net["avg_pool5"] = avg_pool(net["relu5_4"])
    
    return net



