import cv2

img=cv2.imread("f4.jpg")
img=cv2.resize(img,(600,500))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inv_gray=255-gray
blur=cv2.GaussianBlur(inv_gray,(11,11),0)
inv_blur=255-blur
photo_sketch=cv2.divide(gray,inv_blur,scale=255)

cv2.imshow("img",img)
cv2.imshow("photo_sketch",photo_sketch)
#cv2.imshow("inv_imgray",inv_gray)
cv2.waitKey(0)
