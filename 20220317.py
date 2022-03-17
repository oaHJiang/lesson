import cv2
img=cv2.imread('p1.jpg')
#path='C:\Users\TEMP.DESKTOP-SS6QN3F.000\AppData\Local\Programs\Python\Python310\Lib\site-packages\cv2\data'
face=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces=face.detectMultiScale(img,scaleFactor=1.07,minNeighbors=12)
for (x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
cv2.imshow('show',img)
cv2.waitKey(0)
cv2.destroyAllWindows()