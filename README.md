# Hand-Gesture-Robot-Control

This project was our team's final project for EEE 511: Artificial Neural Computation. The purpose of this project was to create a CNN that could be used to control a UR10e robotic arm. This README outlines the steps necessary to run the project on your own platform with the following **Requirements**:

## Requirements
- System Requirements:
    - Network Connection to the Robot
    - Python Installation
    - What we used:
        - Asus Zephyrus 14 Laptop
        - Ryzen 9 5900 series processor
        - NVIDIA GeForce RTX 3060 40GB of RAM
        - 2 Terabyte hard drive
        - An external camera 1080 pixel wide-angle lens 
        - wireless nano router 
        - External Wifi adapter
- Software Dependencies:
    - Keras
    - Tensorflow
    - Numpy
    - PIL
    - Sklearn
    - Pandas
    - Matplotlib
    - Datetime
    - os

## Steps for Running the Project 
1. Install Dependencies
2. Clone Repository Here: https://github.com/EEE511-Hand-Gesture-Control/Hand-Gesture-Robot-Control
3. Connect to the robot’s network via ethernet or WiFi
4. Ensure computer has access to a camera (internal or external)
5. Run “robotControlFromImageRec.py”
6. Gesture in front of camera and verify robot output


## Explanation for each Script

**TODO**

## Steps for connecting to the Robot
1. Connect ethernet cable or wireless router to the ethernet port on the Robot's control box.
2. Connect the other end of the ethernet cable to the computer or connect the computer's wireless network to the router transmitting from the control box.
3. Place the robot into Remote Mode. 
- 3.1) This mode option is found under the Robot's settings in the upper right corner of the teach pendant.
4. To verify the connection, you can ping the robot from the command window. You can also use the socketTest application to verify the live connection with the robot. 
5. Once the robot is connected, it's ready to run the script.


Dataset can be found: https://drive.google.com/file/d/1tn2k9fgBaPjvQgBO5YIVZOwub-MLljan/view?usp=sharing
