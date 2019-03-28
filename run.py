#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:27:03 2019

@author: bruno
"""
import numpy as np
import tensorflow as tf
import cv2

import vrep
from Model import Topology

def set_velocity(handle, velocity):                
        return vrep.simxSetJointTargetVelocity(
                clientID,
                handle,
                velocity,
                vrep.simx_opmode_streaming
                )

def process_img(img):
    img = cv2.resize(img, (227, 227));   
    img = img[1:225,1:225,:];
    img = np.expand_dims(img, axis=0)    
    return img
               

model = 'Model/model.npy';

image_scores = np.reshape([np.random.rand(1)[0] for i in range(61)], (61,1))

input_node = tf.placeholder(tf.float32, shape=(None, 224, 224, 3));
nn = Topology({'data': input_node})

config=tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allow_growth=True

sesh = tf.Session(config=config)
nn.load(model, sesh)

velocity = 8
nitro_gain = 3

freeze_recog = True

cap = cv2.VideoCapture(0)

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',20000,True,True,5000,5)

while cv2.waitKey(1) != ord('q'):
    
    _, frame = cap.read()
    frame = cv2.resize(frame, (320,240))
    image_scores = sesh.run(nn.get_output(), feed_dict={input_node: process_img(frame)})
    
    pred = np.argmax(image_scores, axis=1)[0];
    
    image_scores.sort()
    prediction_score = image_scores[0][-1]
    
    if(prediction_score > 0.85):        
        _, leftMotorID = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_blocking)
        _, rightMotorID = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_blocking)
                
        if pred == 1 and not freeze_recog:
            print("START")
        
            set_velocity(leftMotorID, velocity)
            set_velocity(rightMotorID, velocity)
        
        if pred == 3 and not freeze_recog:
            print("REAR")
        
            set_velocity(leftMotorID, -velocity)
            set_velocity(rightMotorID, -velocity)
        
        if pred == 36 and not freeze_recog:
            print("NITROOO!!!")
        
            set_velocity(leftMotorID, nitro_gain*velocity)
            set_velocity(rightMotorID, nitro_gain*velocity)
            
        elif pred == 2 and not freeze_recog:
            print("STOP")
        
            set_velocity(leftMotorID, 0)
            set_velocity(rightMotorID, 0)
            
        elif pred == 6 and not freeze_recog:
            print("ROTATING ANTI-CLOCKWISE : FROM 1")
            set_velocity(rightMotorID, velocity)
            set_velocity(leftMotorID, velocity/2)
            
        elif pred == 11 and not freeze_recog:
            print("ROTATING CLOCKWISE : FROM 1")
            set_velocity(rightMotorID, velocity/2)
            set_velocity(leftMotorID, velocity)
            
        elif pred == 20 and not freeze_recog:
            print("FREEZED RECOGNITION")
            freeze_recog = True
            set_velocity(rightMotorID, 0)
            set_velocity(leftMotorID, 0)
            
        elif pred == 10 and freeze_recog:
            print("UNFREEZED RECOGNITION")
            freeze_recog = False
            set_velocity(rightMotorID, 0)
            set_velocity(leftMotorID, 0)
        
    cv2.imshow('f1',frame)    

cap.release()
cv2.destroyAllWindows()        

#%%
