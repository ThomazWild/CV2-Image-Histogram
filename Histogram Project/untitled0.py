# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:00:49 2019

@author: thewo
"""

import numpy as np
import cv2

img = cv2.imread('image.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()