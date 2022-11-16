

import cv2
import numpy as np
import matplotlib.pyplot as plt



from quantizeHSV import quantizeHSV
from quantizeRGB import quantizeRGB
from computeQuantizationError import computeQuantizationError
from getHueHists import getHueHists



origImg = cv2.imread('fish.jpg')
origImg = cv2.cvtColor(origImg, cv2.COLOR_BGR2RGB)

k_values=[2,5,8]

for k in k_values:
    rgb = quantizeRGB(origImg , k)
    plt.figure(10*k +1)
    plt.imshow(rgb)
    plt.title("Quantized RGB image with k: {}".format(k))
    
    print("SSD for RGB image quantized with K ={}: ".format(k),end='')
    print(computeQuantizationError(origImg , rgb))
    
    hsv,centers = quantizeHSV(origImg , k)
    plt.figure(10*k +2)
    plt.imshow(hsv)
    plt.title("Quantized HSV image with k: {}".format(k))
    
    print("SSD for HSV image quantized with K ={}: ".format(k),end='')
    print(computeQuantizationError(origImg , hsv))
    
    hcolumn , outputHcolumn = getHueHists(origImg , k)
    plt.figure(10*k +3)
    plt.hist(hcolumn)
    plt.title("Histogram - Uniform bins with k: {}".format(k))
    
    plt.figure(10*k + 4)
    plt.hist(outputHcolumn)
    plt.title("Histogram - Hue Clustered bins with k: {}".format(k))
    
    plt.show()
    

  