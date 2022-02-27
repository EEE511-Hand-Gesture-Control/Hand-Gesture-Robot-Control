# Control for UR10e with Hand Gesture Recognition ![SHIELD](https://img.shields.io/badge/Project%20Status%3A-Complete-green?style=for-the-badge) ![PYTHON](https://camo.githubusercontent.com/3df944c2b99f86f1361df72285183e890f11c52d36dfcd3c2844c6823c823fc1/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d507974686f6e26636f6c6f723d333737364142266c6f676f3d507974686f6e266c6f676f436f6c6f723d464646464646266c6162656c3d) ![ROBOTICS](https://camo.githubusercontent.com/b8e2732eda54a502cb34a56c1ea83747134ce98754e6c49a3177cd89f411bc97/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d526f626f742b4672616d65776f726b26636f6c6f723d303030303030266c6f676f3d526f626f742b4672616d65776f726b266c6f676f436f6c6f723d464646464646266c6162656c3d) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

## About
This project was our team's final project for EEE 511: Artificial Neural Computation. The purpose of this project was to create a CNN that could be used to control a UR10e robotic arm. This README outlines the steps necessary to run the project on your own platform with the following:

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

### 511Model.py
This script contains everything necessary for dataset preprocessing, model setup, model training, and model evalution. The script will conclude by generating a confusion matrix and saving the model in a directory called 'saved_model'.

### ImageDataGenerator.py
This script was used to generate the team's dataset. The script will guide the user through taking the images and going through the gestures. It will also perform all of the augmentations. After completion, the generated dataset will be stored locally.

### ImagePredictor.py
This script contains the preprocessing function for the preprocessing needed to take live images from the webcam and process them into a format that can be fed to the neural network.

### robotControlFromImageRec.py
This script contains the implementation of the project. It establishes a socket connection with a robot arm at a certain IP address. It then pulls images from a webcam, processes them, passes them into the model, and then outputs the respective action to the robot arm.

## Steps for connecting to the Robot
1. Connect ethernet cable or wireless router to the ethernet port on the Robot's control box.
2. Connect the other end of the ethernet cable to the computer or connect the computer's wireless network to the router transmitting from the control box.
3. Place the robot into Remote Mode. 
- 3.1) This mode option is found under the Robot's settings in the upper right corner of the teach pendant.
4. To verify the connection, you can ping the robot from the command window. You can also use the socketTest application to verify the live connection with the robot. 
5. Once the robot is connected, it's ready to run the script.

## Dataset
Dataset can be found: https://drive.google.com/file/d/1tn2k9fgBaPjvQgBO5YIVZOwub-MLljan/view?usp=sharing
