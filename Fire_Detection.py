# Fire_Detection
import cv2
import numpy as np
video = cv2.VideoCapture(0)
while True:
    (grabbed, frame)= video.read()
    if not grabbed:
        break
    blur= cv2.GaussianBlur(frame,(21,21),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower = [18,50,50]
    upper = [35,255,255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask= cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, hsv, mask=mask)
    no_red=cv2.countNonZero(mask)
    cv2.imshow("output", output)
    if int(no_red)>50000:
        print("Fire detected")
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
cv2.destroyAllWindows()
video.release()
Firebase data push and pull:
import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os 
from functools import partial
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
firebase = firebase.FirebaseApplication('https://project-d4cc5.firebaseio.com/', None)
def update_firebase():
	if(human_detected || fire_detected || bomb_detected):
		Alarm = “Yes”
	else:
		print('Failed to get reading. Try again!')	
		sleep(10)
while True:
	data = {"Yes": alarm}
	firebase.del('/alarm', data)
	firebase.post('/alarm', data)	
##while True:
	update_firebase()	
	sleep(5)

