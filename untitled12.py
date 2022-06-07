# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BlDn4IBrhhMYrTKGDfmvIKzvuTW_bUJ_
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img=np.zeros((100,500),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX
img1=cv2.putText(img,'AmarNath',(10,80),font,1.4,(200),5,cv2.LINE_AA)
plt.imshow(img1)

Kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11))

image1=cv2.morphologyEx(img,cv2.MORPH_OPEN,Kernel)
plt.imshow(image1)

image1=cv2.morphologyEx(img,cv2.MORPH_CLOSE,Kernel)
plt.imshow(image1)