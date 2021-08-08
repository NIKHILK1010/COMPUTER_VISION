import pytesseract
import cv2
img=cv2.imread("Number_plate.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny_img=cv2.Canny(gray,170,200)
contour,new=cv2.findContours(canny_img.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contour=sorted(contour,key=cv2.contourArea,reverse=True)[:30]

contour_license_plate=None
license_plate=None
x=None
y=None
w=None
h=None

for c in contour:
    perimeter=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.01*perimeter,True)
    if len(approx)==4:
        contour_license_plate=approx
        x,y,w,h=cv2.boundingRect(c)
        license_plate=gray[y:y+h,x:x+w]
        break

license_plate=cv2.bilateralFilter(license_plate,11,17,17)
(thres,license_plate)=cv2.threshold(license_plate,150,180,cv2.THRESH_BINARY_INV)

text=pytesseract.image_to_string(license_plate)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
img=cv2.putText(img,text,(x-100,y-50),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,0,0),2)
print(text)

cv2.imshow("img",img)
cv2.waitKey(0)
