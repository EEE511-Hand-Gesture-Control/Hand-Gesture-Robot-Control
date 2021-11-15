# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:58:33 2021

@author: olivi
"""
#control a UR Robot with gesture inputs

import socket #to set commands to the UR
import time
from ImagePredictor import predict_with_label
import tensorflow as tf
import os
import cv2
import numpy as np
import time


class driveUR:	
    
    #Initialization
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bindUR()
        self.speedX = 0.00
        self.speedY = 0.00
        self.speedZ = 0.00
        self.acceleration = 1
        self.keys = [0, 0, 0]
        print('init')
        
    #connecting to the UR IP
    def bindUR(self):
        print(self.s.connect(("192.168.1.25",30003)))
    
    #sending the data: is a conviance thing to add the new line after
    def send_to_ur(self,data):
        print(data)
        self.s.send(data.encode())
        self.s.send("\n\r".encode())
    
    #builds the data that needs to be sent
    def build_packet(self, directionVector):
        #this is the script to make the UR move, with speedl(the direction variable, the acceleration, and a 1 s timeout      
        return str("speedl(["+str(directionVector)+"],"+str(self.acceleration)+",1)")
    #builds the vector
    def vector_build(self, x,y,z,xr,yr,zr):
        vectorOutput = ""
        #concatinates the component values
        vectorOutput = str(x) + "," + str(y) + "," + str(z) + "," + str(xr) + "," + str(yr) + "," + str(zr)
        return vectorOutput
    #makes life easy
    def sendVector2UR (self, x,y,z,xr,yr,zr):
        go.send_to_ur(go.build_packet(go.vector_build(x, y, z, xr, yr, zr)))

    def gestureRec(self, gesture_prediction): #I want to use the output of ImagePredictor as the input
        #take the predicted gesture and assign the corresponding keys tag
        if gesture_prediction == "Pointing Right": #+x
            self.keys = [1, 0, 0]
            print("Robot Command: Pointing Right")
        elif gesture_prediction == "Peace": #-x
            self.keys = [-1, 0, 0]
            print("Robot Command: Peace")
        elif gesture_prediction == "Thumbs Up": #+y
            self.keys = [0, 1, 0]
            print("Robot Command: Thumbs Up")
        elif gesture_prediction == "Thumbs Down": #-y
            self.keys = [0, -1, 0]
            print("Robot Command: Thumbs Down")
        elif gesture_prediction == "Palm": #+z
            self.keys = [0, 0, 1]
            print("Robot Command: Palm")
        elif gesture_prediction == "Back of Hand": #-z
            self.keys = [0, 0, -1]
            print("Robot Command: Back of Hand")
        elif gesture_prediction == "Blank":
            self.keys = [0, 0, 0]
            print("Robot Command: Blank")
        else:
            print("Other Command, Sticking to Previous Command")
            
    
    #manages the arrage to send the robot based off bit
    def jogRobot(self):
        tSpeedX = 0
        tSpeedY = 0
        tSpeedZ = 0
        tSpeedX = self.speedX * self.keys[0]
        tSpeedY = self.speedY * self.keys[1]
        tSpeedZ = self.speedZ * self.keys[2]
        print(f'X Speed: {tSpeedX}')
        print(f'Y Speed: {tSpeedY}')
        print(f'Z Speed: {tSpeedZ}')
        self.sendVector2UR(tSpeedX, tSpeedY, tSpeedZ, 0, 0, 0)#sends the UR the calculated speed vectors based on key press
        if tSpeedX == 0:
            self.speedX = 0.005 #initial speed setting of 5mm/sec
        else:
            self.speedX = self.speedX + 0.002 #increase speed the longer the button is pressed
        if tSpeedY == 0:
            self.speedY = 0.005 #initial speed setting of 5mm/sec
        else:
            self.speedY = self.speedY + 0.002 #increase speed the longer the button is pressed
        if tSpeedZ == 0:
            self.speedZ = 0.005 #initial speed setting of 5mm/sec
        else:
            self.speedZ = self.speedZ + 0.002 #increase speed the longer the button is pressed
        


if __name__ == '__main__':
    
    model = tf.keras.models.load_model(r'saved_model/model2021-11-08')

    print(model.summary())

    cap = cv2.VideoCapture(0)
    time.sleep(2)
    go = driveUR()
    
    while(1):
        ret, frame = cap.read()
        cv2.imshow('my webcam', frame)
        if ret:
            gesture_prediction = predict_with_label(model, frame)
            go.gestureRec(gesture_prediction)
            go.jogRobot()
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(0.01)
    cap.release()
    cv2.destroyAllWindows()