# Opening-and-Closing

## Aim
To implement Opening and Closing using Python and OpenCV.

## Software Required
1. Anaconda - Python 3.7
2. OpenCV
## Algorithm:
Step 1:
### Import the necessary packages.<br>

### Step 2:
Create the Text using cv2.putText.<br>

### Step 3:
Create the structuring element.<br>

### Step 4:
Use Opening operation.<br>

### Step 5:
Use Closing Operation.<br>

 
## Program:
## developed by: Amarnath Reddy.<br>
## regestration no:212221240012.<br>

``` Python
# Import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plt
# Create the Text using cv2.putText
img1=np.zeros((100,500),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
im=cv2.putText(img1,' SAI DARSHAN ',(5,70),font,2,(255),5,cv2.LINE_AA)
# Create the structuring element
Kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11))
# Use Opening operation
image1=cv2.morphologyEx(im,cv2.MORPH_OPEN,Kernel)
plt.imshow(image1)
# Use Closing Operation
image1=cv2.morphologyEx(im,cv2.MORPH_CLOSE,Kernel)
plt.imshow(image1)

```
## Output:

### Display the input Image

![1](https://user-images.githubusercontent.com/94165103/172443377-e7c1d10b-96fb-4466-93a9-b0e2f65e3aef.png)

### Display the result of Opening

![2](https://user-images.githubusercontent.com/94165103/172443459-e98b02c5-bb06-45c1-8b91-b6985590222d.png)

### Display the result of Closing

![3](https://user-images.githubusercontent.com/94165103/172443551-2da54c5b-0bbd-40e2-82ad-720aacded53f.png)

## Result
Thus the Opening and Closing operation is used in the image using python and OpenCV.
