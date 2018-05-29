import cv2
import numpy as np

#function to return sketch using webcam

def sketch(img):

    #coverting Color to gray scale
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Applying Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img,(5,5),0)

    #Edge detection
    img_edge = cv2.Canny(img_gray_blur,10,80)

    #Applying Threshold and Inverting
    ret,final_img = cv2.threshold(img_edge,70,255,cv2.THRESH_BINARY_INV)
    return final_img

#Starting up the web cam
cam = cv2.VideoCapture(0)

while True:
    ret,on_screen = cam.read()
    sketch_img = sketch(on_screen)
    if cv2.waitKey(1) == 13:
        cv2.imwrite('My_Sketch'+'.png',sketch_img)
    cv2.imshow('Your Sketch',sketch_img)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
    
