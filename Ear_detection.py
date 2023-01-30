import cv2
image = cv2.imread('holly.jpg')
classifier =cv2. CascadeClassifier('haarcascade_mcs_rightear.xml')
boxes = classifier.detectMultiScale(image)
for box in boxes:
 x, y, width, height = box
 x2, y2 = x + width, y + height
 cv2.rectangle(image, (x, y), (x2, y2), (0,255,0), 5)
cv2.imshow('ear detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()