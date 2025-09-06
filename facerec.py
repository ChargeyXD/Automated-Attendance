import cv2 as cv

vid = cv.VideoCapture(0)
vid.set(3, 1280)
vid.set(4, 680)

while True:
    success, img = vid.read()
    cv.imshow("Webcam", img)
    cv.waitKey(1)
