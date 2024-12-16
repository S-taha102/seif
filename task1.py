import numpy as np
import cv2 as cv


img1 = np.zeros([50, 50, 3], np.uint8)
img2 = np.zeros([50, 50, 3], np.uint8)
img3 = np.zeros([50, 50, 3], np.uint8)
img4 = np.zeros([50, 50, 3], np.uint8)


img1[:] = [255, 0, 0]     
img2[:] = [0, 0, 255]     
img3[:] = [0, 255, 0]     
img4[:] = [255, 0, 255]   


top = np.hstack((img1, img2))   
bottom = np.hstack((img3, img4))  

image = np.vstack((top, bottom))  
resize=cv.resize(image,(200,200))


cv.imshow('image', resize)
cv.waitKey(0)
cv.destroyAllWindows()
