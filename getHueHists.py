
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt


def getHueHists(origImg,k):
  # Returns histEqual, histClustered
  
  hsv_im =  cv2.cvtColor(origImg , cv2.COLOR_RGB2HSV)  
  
  hsv_array = hsv_im.reshape((-1, 3))
  
  hsv_array = np.float32(hsv_array)
  hcolumn  = hsv_array[:,0].copy()
  
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1000, 0.09)
  _, labels, (centers) = cv2.kmeans(hcolumn, k,None ,criteria = criteria , attempts = 10, flags = cv2.KMEANS_RANDOM_CENTERS)
  centers = np.uint8(centers)
  labels = labels.flatten()
  outputHcolumn  = centers[labels.flatten()]
  
  
  return hcolumn, outputHcolumn
  
