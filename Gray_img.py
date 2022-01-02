import cv2 as cv

img=cv.imread('images/hero.png')
Gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('image',Gray_img)
cv.waitKey(0)

