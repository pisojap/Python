import numpy as np
import cv2
import glob

images = glob.glob("srcFolder\\*.jpg")

for image in images:
    img = cv2.imread(image ,1)
    resizedImage = cv2.resize(img, (100, 100))
    cv2.imwrite(image + ".100.jpg", resizedImage)
