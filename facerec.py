import cv2 as cv

def Webcam():
    vid = cv.VideoCapture(0)
    vid.set(3,1280)
    vid.set(4, 720)

    while True:
        success, img = vid.read()
        ret, buffer = cv.imencode('.jpg',img)
        img = buffer.tobytes()
        return img