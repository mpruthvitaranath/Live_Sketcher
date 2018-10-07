import cv2
 
num_down = 3      
num_bilateral = 6  

img_rgb = cv2.imread("img4578.jpg")
 
img_color = img_rgb
for kl in xrange(num_down):
    img_color = cv2.pyrDown(img_color)
 
for kx in xrange(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=9,
                                    sigmaColor=9,
                                    sigmaSpace=7)
 
for kj in xrange(num_down):
    img_color = cv2.pyrUp(img_color)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=9,
                                 C=2)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color, img_edge)
 
cv2.imshow("Cartoon_Effect", img_cartoon)