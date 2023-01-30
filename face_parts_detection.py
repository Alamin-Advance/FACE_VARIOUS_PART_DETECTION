# import libraries
import cv2
import numpy as np
#read the image
image = cv2.imread('lena.jpeg')
# show the original read image
cv2.imshow("original image",image)

#load the xml files for face, eye and mouth detection into the program
classifier_f =cv2. CascadeClassifier('haarcascade_frontalface_default.xml')
classifier_n =cv2. CascadeClassifier('haarcascade_mcs_nose.xml')
classifier_e =cv2. CascadeClassifier('haarcascade_eye.xml')
classifier_m =cv2. CascadeClassifier('haarcascade_mcs_mouth.xml')

#identify the face using haar-based classifiers
bboxes_f = classifier_f.detectMultiScale(image)
#iteration through the face array and draw a rectangle
for box in bboxes_f:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    cv2.rectangle(image, (x, y), (x2, y2), (0,255,0), 2)

#identify the nose using haar-based classifiers
bboxes_n = classifier_n.detectMultiScale(image)
#iteration through the nose array and draw a rectangle
for box in bboxes_n:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    cv2.rectangle(image, (x, y), (x2, y2), (0,255,0), 2)

#identify the eye using haar-based classifiers
bboxes_e = classifier_e.detectMultiScale(image)
#iteration through the eye array and draw a rectangle
for box in bboxes_e:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    cv2.rectangle(image, (x, y), (x2, y2), (0,0,255), 2)

#identify the mouth using haar-based classifiers
bboxes_m = classifier_m.detectMultiScale(image)
#iteration through the mouth array and draw a rectangle
for box in bboxes_m:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    cv2.rectangle(image, (x, y), (x2, y2), (255,0,0), 2)

#show the final image after detection
img=cv2.imshow('face,nose,eye and mouth detection image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()