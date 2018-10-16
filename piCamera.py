#!/usr/bin/python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Loop is created for redundancy
# The recording time is 3 hours

i= 36
<<<<<<< HEAD
print("Pi camera initialized \n")
while i > 0:

    camera.start_preview()
    camera.start_recording(str(i)+'.h264')
    print('Video Number '+str(i)+' started \n')
    i=i-1    
    sleep(300)
    camera.stop_recording()
    camera.stop_preview()
    
    print('Video Number ' +str(i)+' completed \n')

=======
print("Pi camera initialized")
if i == 36:
    camera.start_preivew()
    sleep(5)
    camera.start_recording()
    sleep(300)
    camera.stop_recording()
    camera.stop_preview()
    i=i-1
    print("Pi camera test run completed and logged")
elif i > 0:
    camera.start_preview()
    camera.start_recording()
    sleep(300)
    camera.stop_recording()
    camera.stop_preview()
    i=i-1

