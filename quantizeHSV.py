import cv2
import numpy as np

def quantizeHSV(origImg, k):
  '''
  returns outpoutImg, meanHues
  '''
  #convert to HSV
  hsvImage = cv2.cvtColor(origImg, cv2.COLOR_RGB2HSV)

  #Quantize H space with k
  flattened_image = hsvImage.reshape((-1, 3))
  flattened_image = np.float32(flattened_image)
  flattened_image_old = flattened_image.copy()
  hcolumn  = flattened_image_old[:,0]
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1000, 0.09)
  tr, labels, (centers) = cv2.kmeans(hcolumn, k,None ,criteria = criteria , attempts = 10, flags = cv2.KMEANS_RANDOM_CENTERS)
  centers = np.uint8(centers)
  labels = labels.flatten()
  outputHsv  = centers[labels.flatten()]
  # Replace the H column
  flattened_image[:,0] = outputHsv.flatten()
  flattened_image = np.uint8(flattened_image)
  outputHsvImg = flattened_image.reshape(origImg.shape)
  #Convert back to RGB
  outputImg = cv2.cvtColor(outputHsvImg, cv2.COLOR_HSV2RGB)
  
  return outputImg , centers