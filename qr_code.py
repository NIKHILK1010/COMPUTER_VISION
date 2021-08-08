import cv2

img=cv2.imread('qr.jpg')
detection=cv2.QRCodeDetector()

data=detection.detectAndDecode(img)

print(data)
cv2.putText(img,str(data),(20,60),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.22,(0,0,255),2)
#cv2.rectangle(img,(500,200),(300,400),(255,0,0),2)
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
