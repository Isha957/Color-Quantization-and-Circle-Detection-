import numpy as np


def computeQuantizationError(origImg , quantizedImg):
  #returns error
  assert origImg.shape == quantizedImg.shape
  #origImg = np.float32(origImg)
  #quantizedImg = np.float32(quantizedImg)
  
  return np.sum((np.array(origImg, dtype=np.float32) - np.array(quantizedImg, dtype=np.float32))**2)


