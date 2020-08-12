# Face Detection
import numpy as np
import cv2
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()
# open webcam video stream
cap = cv2.VideoCapture(0)
# the output will be written to output.avi
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    # Write the output video 
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
Bot Motion:
import RPi.GPIO as GPIO
import socket
import csv
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.output(29,True)
GPIO.output(31,True)
UDP_IP = "0.0.0.0"
UDP_PORT = 5050
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))
while True:
data, addr = sock.recvfrom(1024)
raw=data
#print raw
if raw=="forward":
GPIO.output(33,True)
GPIO.output(11,False)
GPIO.output(13,True)
GPIO.output(15,False)
print "Robot Move Forward"
elif raw=="stop":
GPIO.output(33,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)
print "Robot Stop"
elif raw=="backward":
GPIO.output(33,False)
GPIO.output(11,True)
GPIO.output(13,False)
GPIO.output(15,True)
print "Robot Move Backward"
elif raw=="left":
GPIO.output(33,False)
GPIO.output(11,True)
GPIO.output(13,True)
GPIO.output(15,False)	
print "Robot Move Left"
elif raw=="right":
GPIO.output(33,True)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,True)	
print "Robot Move Right"
else:
print "STOP"
GPIO.output(33,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)
