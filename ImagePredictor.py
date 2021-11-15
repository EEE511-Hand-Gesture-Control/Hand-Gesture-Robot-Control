#!/usr/bin/python3
"""
TO USE:
Place this file in same directory as main py file.
Put following import:
from ImagePredictor import predict_with_label
In main code:
print(predict_with_label(model, image))
where model is the NN and image is the capture
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import PIL
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#os.chdir(r"C:\Users\super\OneDrive - Arizona State University\EEE 511 Artificial Neural Comp\hand_gesture_recognition")
hand_gesture_recog_dict = {
    1  : "Okay",
    2  : "Thumbs Up",
    3  : "Thumbs Down",
    4  : "Pointing Right",
    5  : "Blank",
    6  : "Palm",
    7  : "Back of Hand",
    8  : "Fist",
    9  : "O",
    10 : "Peace"
}

#%%
def pre_process(image, show=0, resize_ratio=(320,120),
                reshape_ratio=(1,120,320,1)):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    proc_img = PIL.Image.fromarray(image)
    proc_img = proc_img.convert('L').resize(resize_ratio)
    proc_img = np.array(proc_img, dtype = 'float32').reshape(reshape_ratio)
    proc_img /= 255
    if show:
        plt.imshow(image)
        plt.show()  
    return proc_img

    
def predict_with_label(model, img, show=0):
    prediction = model.predict(pre_process(img, show=show))
    #print(f'Probability: {max(max(prediction))}%')
    return hand_gesture_recog_dict[prediction.argmax() + 1]

    
if __name__ == '__main__':
    model = tf.keras.models.load_model('model2021-09-28')
    img = PIL.Image.open('leapGestRecog/01/03_fist/frame_01_03_0001.png')
    print(predict_with_label(model, img, show=1))
