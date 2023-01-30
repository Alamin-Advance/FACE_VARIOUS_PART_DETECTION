import cv2
image = cv2.imread('lena.jpeg')
cv2.imshow("original image",image)
classifier_f =cv2. CascadeClassifier('haarcascade_frontalface_default.xml')

bboxes_f = classifier_f.detectMultiScale(image)
for box in bboxes_f:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    cv2.rectangle(image, (x, y), (x2, y2), (0,255,0), 2)
cv2.imshow('face detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()