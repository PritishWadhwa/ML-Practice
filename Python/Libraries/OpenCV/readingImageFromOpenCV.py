import cv2
img = cv2.imread('Pritish.jpg')
greyImg = cv2.imread('Pritish.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Pritish in Grey', greyImg)
cv2.imshow('Pritish', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
