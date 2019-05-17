# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:14:52 2019

@author: thewo
"""
from matplotlib.image import imread
import matplotlib.pyplot as plt

im = imread('image.jpg')
# calculate mean value from RGB channels and flatten to 1D array



plt.imshow(im, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins

b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()
