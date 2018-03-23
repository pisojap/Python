import cv2

faceCascade = cv2.CascadeClassifier("srcFolder/haarcascade_frontalface_default.xml")

img = cv2.imread("srcFolder/news.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grayImg,
                                     scaleFactor=1.1,
                                     minNeighbors=5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
