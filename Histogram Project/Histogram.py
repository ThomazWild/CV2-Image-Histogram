# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:47:38 2019

@author: thewo
"""
from matplotlib.image import imread
from matplotlib import pyplot as plt
#
#import matplotlib as mat
#import plotly.plotly
#import numpy as np

img = imread('image.jpg')

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()