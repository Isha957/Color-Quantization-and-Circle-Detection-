
import cv2
import numpy as np


def quantizeRGB(origImg , k):
    #Returns outputImg , meanColors
    flattened_image = origImg.reshape((-1, 3))
    flattened_image = np.float32(flattened_image)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1000, 0.09)
    tr, labels, (centers) = cv2.kmeans(flattened_image, k,None ,criteria = criteria , attempts = 20, flags = cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    labels = labels.flatten()
    outputImg = centers[labels.flatten()]
    outputImg = outputImg.reshape(origImg.shape)
    return outputImg
    