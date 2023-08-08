import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('watch.jpeg',cv2.IMREAD_COLOR)

##cv2.rectangle(img,(15,25),(200,150),(255,0,0),5)
##cv2.circle(img,(100,63),55,(0,0,255),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'it\'s a watch',(0,130),font,1,(255,0,0),2,cv2.LINE_AA)

##cv2.line(img,(0,0),(150,150),(255,255,255),15) #bgr
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
