import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('watch.jpeg',cv2.IMREAD_COLOR)

##plt.imshow(img,cmap='gray',interpolation='bicubic')
##plt.show()

#50,20 to 170,150

watch_face = img[50:20,170:150]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



