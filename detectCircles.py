


import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve



def detectCircles(img,radius,useGradient):
    #returns centers
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    
    plt.figure(1)
    plt.imshow(img)
    
    # Smooth the image
    guassian_kernel = np.array([[1/16.,1/8.,1/16.],[1/8.,1/4.,1/8.],[1/16.,1/8.,1/16.]])
    img = convolve(img ,guassian_kernel)
    guassian_kernel_t = guassian_kernel.T
    img = convolve(img ,guassian_kernel_t)
    img = cv2.medianBlur(img , 13)
    #Canny Edge detection
    l = 50
    u = 200
    
    L2Gradient = True 
    edge = cv2.Canny(img, l, u, L2gradient = L2Gradient )
    
    plt.figure(2)
    plt.imshow(edge)

    
    
    (M,N) = img.shape
    
    #Initializing accumulator array.
    accumulator_array = np.zeros((M+ 2*radius , N+ 2*radius)) 
    #this 2*radius is required because there might be points with respective cirlces in hough space that go beyond the image limits on either side.
    
    theta = np.arange(0,360,60)*np.pi/180
    edges = np.argwhere(edge[:,:])
    r_cos_thetas = np.round(radius*np.cos(theta))
    r_sin_thetas = np.round(radius*np.sin(theta))
    
    if(not useGradient):
        for x,y in edges:
            newxs = [x+int(p) for p in r_cos_thetas]
            newys = [y+int(p) for p in r_sin_thetas]
            for x1,y1 in zip(newxs , newys):
                accumulator_array[x1][y1] += 1
        
    else:
        sobelx = cv2.Sobel(edge,cv2.CV_64F,1,0) # Find x and y gradients
        sobely = cv2.Sobel(edge,cv2.CV_64F,0,1)

        # Find magnitude and angle
        magnitude = np.sqrt(sobelx**2.0 + sobely**2.0)
        angle = np.arctan2(sobely, sobelx) 
        for x,y in edges:
            angle_at_x_y = angle[x][y]
            cos_angle = np.round(radius*np.cos(angle_at_x_y))
            sin_angle = np.round(radius*np.sin(angle_at_x_y))
            newxs = [x+int(sin_angle) , x-int(sin_angle)]
            newys = [y+int(cos_angle) , y-int(cos_angle)]
            for x1,y1 in zip(newxs , newys):
              accumulator_array[x1][y1] += 1
            
        
        
    
      
    plt.figure(4)
    plt.imshow(accumulator_array)
    plt.title('Accumulator array for radius = {}'.format(radius))
    d2={}
    fig, ax = plt.subplots()
    plt.imshow(img)
    val = 10
    if(useGradient):
        val=0
    for x,y in np.argwhere(accumulator_array>val):
        d2[(x,y)] = accumulator_array[x][y]
    d1 = sorted(d2, key=d2.get, reverse=True)[:5]
    d = {}
    for x,y in d1:
        d[(x,y)] = d2[(x,y)]
        c = plt.Circle((y,x),radius,color=(1,1,1),fill=False)
        ax.add_patch(c)
    plt.title('detected Circle for radius = {}'.format(radius))
    plt.show()
        
    return accumulator_array,d
    '''
    circleCoordinates = np.argwhere(accumulator_array)
    circle = []
    fig = plt.figure()
    for x,y in circleCoordinates:
        circle.append(plt.Circle((y,x),radius,color=(1,0,0),fill=False))
        fig.add_subplot(111).add_artist(circle[-1])
    plt.show()
    return accumulator_array
    '''

img = cv2.imread('jupiter.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

accumulator_array,d = detectCircles(img , 30 , False)

#k = [10,30,50]
#for kval in k:
 #   accumulator_array,d = detectCircles(img , kval , True)



