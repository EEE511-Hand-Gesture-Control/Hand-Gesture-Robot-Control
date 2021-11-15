# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:01:15 2021

@author: olivi
"""

import keras.utils
from tensorflow.keras.utils import to_categorical
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from sklearn.model_selection import train_test_split
from keras import layers, models
import sklearn 
from sklearn.metrics import confusion_matrix
from datetime import date
import tensorflow as tf
from tensorflow import keras
import pandas as pd

#%%
'''
This section creates the dictionaries for the dataset
'''

lookup = dict()
rev_lookup = dict()
count = 0

for j in os.listdir('C:/Users/olivi/.spyder-py3/511 Images/Images/00/'):
  print("j: ", j)
  if not j.startswith('.'): 
      lookup[j] = count
      rev_lookup[count] = j
      count = count + 1
  
x_data = []
y_data = []
datacount = 0 # We'll use this to tally how many images are in our dataset
for i in range(0, 11): # Loop over the ten top-level folders
    for j in os.listdir('C:/Users/olivi/.spyder-py3/511 Images/Images/0' + str(i) + '/'):
        if not j.startswith('.'): # Again avoid hidden folders
            count = 0 # To tally images of a given gesture
            for k in os.listdir('C:/Users/olivi/.spyder-py3/511 Images/Images/0' + 
                                str(i) + '/' + j + '/'):
                                # Loop over the images
                img = Image.open('C:/Users/olivi/.spyder-py3/511 Images/Images/0' + 
                                 str(i) + '/' + j + '/' + k).convert('L')
                                # Read in and convert to greyscale
                img = img.resize((320, 120))
                arr = np.array(img)
                x_data.append(arr) 
                count = count + 1
            y_values = np.full((count, 1), lookup[j]) 
            y_data.append(y_values)
            datacount = datacount + count
x_data = np.array(x_data, dtype = 'float32')
y_data = np.array(y_data)
y_data = y_data.reshape(datacount, 1) # Reshape to be the correct size

print(x_data.shape)
print(datacount)
print(len(y_data))

'''
This section is used to create the dataset, the network architecture, the compiler for
the Keras model, and to train the model with the dataset generated in the previous section
'''

y_data = to_categorical(y_data)
x_data = x_data.reshape((datacount, 120, 320, 1)) #reshaping x_data into the shape that Keras will expect them
x_data = x_data/255 #rescaling image values to be btw 0 and 1


x_train, x_further, y_train, y_further = train_test_split(x_data, y_data, test_size = .3) #split our current x_data (images) and y_data (labels) lists into a proper dataset variable for keras model with an 80/20 train/test split
x_validate, x_test, y_validate, y_test = train_test_split(x_further, y_further, test_size = .67) #split the new x_further set into a test and evaluation dataset 50/50


model = models.Sequential()
model.add(layers.InputLayer(input_shape=(120,320,1))) #input layer to take in image (this can be done in the first Conv2D layer but this way makes it easier to recognize)
model.add(layers.Conv2D(32, (5,5), strides = (2,2), activation = 'relu')) #first convolutional layer, number of filters/output feature maps = 32, conv_kernel is size 5x5, stride is 2x2, activation is relu
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss = 'categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          epochs = 10,
          batch_size = 64,
          verbose = 1,
          validation_data = (x_validate, y_validate))
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
#%%
print(f"Test Accuracy: {accuracy*100}%")
y_pred = model.predict(x_test)

def get_confusion_matrix(y_test, y_pred):
    y_pred = tf.argmax(y_pred, axis = -1)
    y_test = tf.argmax(y_test, axis = -1)
    
    conf_matrix = tf.math.confusion_matrix(labels = y_test, predictions = y_pred)
    conf_matrix = np.matrix(conf_matrix)
    conf_matrix = 100 * sklearn.preprocessing.normalize(conf_matrix, norm="l1")
            
    conf_matrix = conf_matrix.round(2)
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i, s=conf_matrix[i,j], va='center', ha='center', size='xx-large')
    
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    
    plt.show()
        
    return conf_matrix

conf_matrix = get_confusion_matrix(y_test, y_pred)

#%%
'''
This section saves a new Keras model onto the Shared drive folder, with a dirname
that corresponds to the current date

reference: https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/save_and_load.ipynb#scrollTo=sI1YvCDFzpl3
'''

curr_date = date.today()
print("Today's date:", curr_date)

#create tirectory
os.mkdir('saved_model')
dir_name = f'saved_model/model{curr_date}'

#save model in default protobuf binary format
model.save(dir_name)
print(f"Model saved at: {dir_name}")

