import cv2
import os

height = 500
width = 500
size = (width, height)

left_s = cv2.imread("saved_eyes/l1.jpg")
right_s = cv2.imread("saved_eyes/r1.jpg")
left_s = cv2.cvtColor(left_s, cv2.COLOR_BGR2GRAY)
right_s = cv2.cvtColor(right_s, cv2.COLOR_BGR2GRAY)
left_s = cv2.resize(left_s, size)
right_s = cv2.resize(right_s, size)

left_n = cv2.imread("new_eyes/l2.jpg")
right_n = cv2.imread("new_eyes/r2.jpg")
left_n = cv2.cvtColor(left_n, cv2.COLOR_BGR2GRAY)
right_n = cv2.cvtColor(right_n, cv2.COLOR_BGR2GRAY)
left_n = cv2.resize(left_n, size)
right_n = cv2.resize(right_n, size)

errorL2_l = cv2.norm(left_s, left_n, cv2.NORM_L2)
errorL2_r = cv2.norm(right_s, right_n, cv2.NORM_L2)
similarity_l = (1 - errorL2_l/(height * width))*100
similarity_r = (1 - errorL2_r/(height * width))*100
print("Similarity of left eyes: ", similarity_l, "%")
print("Similarity of right eyes: ", similarity_r, "%")

"""
path1 = 'saved_eyes'
path2 = 'new_eyes'
dir_list_saved = os.listdir(path1)
dir_list_new = os.listdir(path2)
"""

"""
for x in dir_list_saved:
    if "l" in x:
        left_s = path1+"/"+x
        print(left_s)
    if "r" in x:
        right_s = x
    left_s = cv2.imread(left_s)
    #right_s = cv2.imread(right_s)
    left_s = cv2.cvtColor(left_s, cv2.COLOR_BGR2GRAY)
    #right_s = cv2.cvtColor(right_s, cv2.COLOR_BGR2GRAY)
    left_s = cv2.resize(left_s, size)
    #right_s = cv2.resize(right_s, size)
    
    for y in dir_list_new:
        if "l" in y:
            left_n = path2+"/"+y
            print(left_n)
        if "r" in y:
            right_n = y
        left_n = cv2.imread("new_eyes/l2.jpg")
        #right_n = cv2.imread(right_s)
        left_n = cv2.cvtColor(left_n, cv2.COLOR_BGR2GRAY)
        #right_n = cv2.cvtColor(right_s, cv2.COLOR_BGR2GRAY)
        left_n = cv2.resize(left_n, size)
        #right_n = cv2.resize(right_s, size)

    errorL2_l = cv2.norm(left_s, left_n, cv2.NORM_L2)
    #errorL2_r = cv2.norm(right_s, right_n, cv2.NORM_L2)
    similarity_l = 1 - errorL2_l/(height * width)
    #similarity_r = 1 - errorL2_r/(height * width)
    print("Left: ", similarity_l)
    #print("Right: ", similarity_r)

for x in dir_list1:
    if "l" in x:
        left = x
    left = cv2.imread(left)
    orig_l = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    new_l = cv2.cvtColor(left_browless, cv2.COLOR_BGR2GRAY)
    orig_l = cv2.resize(orig_l, size)
    new_l = cv2.resize(new_l, size)
    errorL2_l = cv2.norm(orig_l, new_l, cv2.NORM_L2)
    similarity_l = 1 - errorL2_l/(height * width)
    print("Left: ", similarity_l)

for x in dir_list:
    if "r" in x:
        right = x
    orig_r = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
    new_r = cv2.cvtColor(right_browless, cv2.COLOR_BGR2GRAY)
    orig_r = cv2.resize(orig_r, size)
    new_r = cv2.resize(new_r, size)
    errorL2_r = cv2.norm(orig_r, new_r, cv2.NORM_L2)
    similarity_r = 1 - errorL2_r/(height * width)
    print("Right: ", similarity_r)
"""
"""
# not calibrated
original = cv2.Canny(original, 5, 6)
new = cv2.Canny(new, 5, 6)
"""

"""
# shows two compared pictures
cv2.imshow('original', original)
cv2.imshow('new', new)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""