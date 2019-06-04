import tensorflow as tf
import numpy as np


# Funtion for content image loss
def cal_content_loss(p, x):
    # Equation 1 from the paper
    return 0.5 * tf.reduce_sum(tf.pow(x - p, 2))


# Funtion for style image loss
def cal_style_loss(a, x):
    M = a.shape[1] * a.shape[2]
    N = a.shape[3]
    
    # Gram matrix of original image
    A = gram_matrix(a, M, N)
   
    # Gram matrix of generated image
    G = gram_matrix(x, M, N)
    
    # Equation 4 from the paper
    loss = (1 / (4 * (N ^ 2) * (M ^ 2))) * tf.reduce_sum(tf.pow((G - A), 2))
    return loss


# Funtion to get the gram matrix used to calculate style loss
def gram_matrix(x, area, depth):
    # Equation 3 from the paper
    F = tf.reshape(x, (area, depth))
    G = tf.matmul(tf.transpose(F), F)
    return G


