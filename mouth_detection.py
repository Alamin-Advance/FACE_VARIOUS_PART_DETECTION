import cv2

image = cv2.imread('lena.jpeg')
cv2.imshow("original image", image)
classifier_m = cv2.CascadeClassifier('haarcascade_msc_mouth.xml')

bboxes_m = classifier_m.detectMultiScale(image)
for box in bboxes_m:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    cv2.rectangle(image, (x, y), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Eye detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()