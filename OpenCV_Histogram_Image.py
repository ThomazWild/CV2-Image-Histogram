# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:53:12 2019

@author: thewo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')
color = ('b','g','r')


plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()