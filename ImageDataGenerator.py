# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:59:14 2021

@author: levin
"""

#!/usr/bin/python3
import cv2
import os
import time
import shutil
import numpy as np
from random import randint

NUM_OF_IMAGES_PER_GESTURE = 10
CAMERA_CHANNEL = 0
NUM_OF_GESTURES = 10
IMAGE_WAIT_TIME = 0
IMAGE_SHIFTING_LIMIT = 50
IMAGE_ROTATION_LIMIT = 10
BLUR_KERNEL = (10, 10)

hand_gesture_recog_dict = {
    1  : "okay",         # Start
    2  : "thumbs_up",    # +Y
    3  : "thumbs_down",  # -Y
    4  : "point_right",  # +X
    5  : "Blank",        # Stop
    6  : "palm_open",    # +Z
    7  : "back_hand",    # -Z 
    8  : "fist",         # Close EE
    9  : "O",            # Open EE
    10 : "peace",        # -X
}

def invert_image(img):
    return cv2.bitwise_not(img)

def shift_image(img):
    shift_matrix = np.float32([
	        [1, 0, randint(-IMAGE_SHIFTING_LIMIT, IMAGE_SHIFTING_LIMIT)],
	        [0, 1, randint(-IMAGE_SHIFTING_LIMIT, IMAGE_SHIFTING_LIMIT)]
            ])
    return cv2.warpAffine(img, shift_matrix, (img.shape[1], img.shape[0]))

def rotate_image(img):
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    R = cv2.getRotationMatrix2D((cX, cY), randint(-IMAGE_ROTATION_LIMIT, IMAGE_ROTATION_LIMIT), 1.0)
    return cv2.warpAffine(img, R, (w, h))

def flip_image(img):
    return cv2.flip(img, 1)

def blur_image(img):
    return cv2.blur(img, BLUR_KERNEL)

def equalize_histogram_image(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

if __name__ == '__main__':
    name = input("Please enter your name here: ")
    root = f'{name}'
    if os.path.exists(root):
        shutil.rmtree(root)
        print(f'{root} exists, removing now...')
    os.mkdir(root)
    print(f'Making directory {root} now...')

    seconds = IMAGE_WAIT_TIME
    cam_feed = cv2.VideoCapture(CAMERA_CHANNEL,cv2.CAP_DSHOW)
    img_detected, img = cam_feed.read()
    cv2.waitKey(0)
    for gesture in range(0, NUM_OF_GESTURES):
        if gesture + 1 >= 10:
            gesture_directory = f'{root}/{gesture + 1}_{hand_gesture_recog_dict[gesture + 1]}/'
        else:
            gesture_directory = f'{root}/0{gesture + 1}_{hand_gesture_recog_dict[gesture + 1]}/'
        if os.path.exists(gesture_directory):
            shutil.rmtree(gesture_directory)
        print(f'{gesture_directory} exists, removing now...')
        print(f'\nStarting image capture for gesture: {hand_gesture_recog_dict[gesture + 1]}')
        print(f'Storing in directory: {gesture_directory}')
        os.mkdir(gesture_directory)
        for img_num in range(0, NUM_OF_IMAGES_PER_GESTURE):
            seconds = IMAGE_WAIT_TIME
            while (seconds > 0):
                seconds -= 1
                print(f'\r Time until picture {img_num + 1} taken: {seconds}s', end = '') 
                time.sleep(1)
            print(f'\nTaking picture {img_num + 1} now')
                
            #cam_feed = cv2.VideoCapture(CAMERA_CHANNEL,cv2.CAP_DSHOW)
            img_detected, img = cam_feed.read()
            cv2.waitKey()
            cv2.imshow("training Image", img)
            #cv2.waitKey()
            #del(cam_feed)
            if img_detected:
                cv2.imwrite(f'{gesture_directory}/original_{img_num + 1}.jpg', img) 
                print(f'Saved original image {img_num + 1}')
                
                cv2.imwrite(f'{gesture_directory}/shifted_{img_num + 1}.jpg', shift_image(img))
                print(f'Saved shifted image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/rotated_{img_num + 1}.jpg', rotate_image(img))
                print(f'Saved rotated image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/shifted2_{img_num + 1}.jpg', shift_image(img))
                print(f'Saved shifted 2 image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/rotated2_{img_num + 1}.jpg', rotate_image(img))
                print(f'Saved rotated 2 image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/shifted3_{img_num + 1}.jpg', shift_image(img))
                print(f'Saved shifted 3 image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/rotated3_{img_num + 1}.jpg', rotate_image(img))
                print(f'Saved rotated 3 image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/shifted4_{img_num + 1}.jpg', shift_image(img))
                print(f'Saved shifted 4 image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/rotated4_{img_num + 1}.jpg', rotate_image(img))
                print(f'Saved rotated 4 image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/flipped_{img_num + 1}.jpg', flip_image(img))
                print(f'Saved flipped image {img_num + 1}')
                cv2.imwrite(f'{gesture_directory}/blurred_{img_num + 1}.jpg', blur_image(img))
                print(f'Saved blurred image {img_num + 1}')
                
                print('\n')
            else:
                print("No image detected...\n")
            img_num += 1
        gesture += 1
    print('Process Complete!')