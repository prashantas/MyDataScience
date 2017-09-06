# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:33:48 2017

@author: prassha
"""

import matplotlib.image as mpimg
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

fileName = dir_path + "/MarshOrchid.jpg"

# Load the image
image = mpimg.imread(fileName)
print("Shape:",image.shape)

#You can view the current image using pyplot, like so:
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()

import tensorflow as tf
x = tf.Variable(image)

model = tf.global_variables_initializer()

with tf.Session() as session:
    x= tf.transpose(x,perm=[1,0,2])
    session.run(model)
    result =session.run(x)
    
plt.imshow(result)
plt.show()
