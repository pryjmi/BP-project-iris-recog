import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('algs/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('algs/haarcascade_eye.xml')
detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)

img = cv2.imread("pics/face2.jpeg")

def detect_faces(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0,0,0,0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x,y,w,h) in biggest:
        frame = img[y:y+h, x:x+w]
    return frame

def detect_eyes(img, cascade):  
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)
    width = np.size(img, 1)
    height = np.size(img, 0)
    for (x,y,w,h) in eyes:
        eyecenter = x+w/2
        if eyecenter < width*0.5:
            left_eye = img[y:y+h, x:x+w]
        else:
            right_eye = img[y:y+h, x:x+w]
    return left_eye, right_eye

def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height/5)
    eyebrow_w = int(width/5)
    img = img[eyebrow_h:height-eyebrow_h, eyebrow_w:width-eyebrow_w]
    return img

"""
def blob_process(img, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, 25, 100, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    return img
"""

face = detect_faces(img, face_cascade)
left, right = detect_eyes(face, eye_cascade)
left_browless = cut_eyebrows(right)
right_browless = cut_eyebrows(left)

directory = r'new_eyes'
os.chdir(directory)

print("Input the number of the left eye:")
pic_name = input()
pic_name = "l" + pic_name + ".jpg"
cv2.imwrite(pic_name, left_browless)

print("Input the number of the right eye:")
pic_name = input()
pic_name = "r" + pic_name + ".jpg"
cv2.imwrite(pic_name, right_browless)

#keypoints = blob_process(right_browless, detector)
#keypoints2 = blob_process(left_browless, detector)
#cv2.drawKeypoints(left_browless, keypoints2, left_browless, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.drawKeypoints(right_browless, keypoints, right_browless, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imshow('image', img)
#cv2.imshow('face', face)
#cv2.imshow('left eye', left)
#cv2.imshow('right eye', right)
"""
cv2.imshow('left browless', left_browless)
cv2.imshow('right browless', right_browless)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""