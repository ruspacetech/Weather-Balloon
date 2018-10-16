#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 5
ECHO = 17
file_object = open("UDS_Data.txt", "w")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(2)
i = 20000
def Distance_Calc():
	time.sleep(0.1)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()
	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	file_object.write('Distance:{0!r}cm \n'.format(distance))
while i>0:
	Distance_Calc()
	time.sleep(1)
	i=i-1
	if i==19999:
		print('UDS is operating normally')
#GPIO.cleanup
=======

import csv
#setting a starting condition for the wile loop at the bottom
g = 1
#setting GPIO mode to read input from UDS

print("Setting UDS mode")
GPIO.setmode(GPIO.BCM)

#setting definition for pins
distArray = []
GPIO_TRIGGER = 18
GPIO_ECHO = 24

def distance():
   #initially setting trigger to high
   GPIO.output(GPIO_TRIGGER, True)

   #setting trigger to low after 0.01ms

   time.sleep(0.00001)
   GPIO.output(GPIO_TRIGGER, False)

   StartTime = time.time()
   StopTime= time.time()

   #Saving start time
   while GPIO.input(GPIO_ECHO) == 0:
       StartTime = time.time()
   while GPIO.input(GPIO_ECHO) == 1:
       StopTime = time.time()

   #calculating the distance using the time oit take for the sound wave to go to object and back

   TimeElapsed = StartTime-StopTime

   #The calculation needed to find the distance

   distance = (TimeElapsed*34300)/3
   return distance

print("UDS definition applied")

print("UDS initialized")
if g == 1:
   try:
       dist = distance()
       distArray.append(dist)
       print("Measured Distance = %.1f cm" % dist)
       time.sleep(0.1)
   except KeyboardInterrupt:
       print("Measurement Stopped")
       GPIO.cleanup()
dists = str(distArray)
myFile = open('UDSlog', 'w')

with myFile:
   writer = csv.writer(myFile)
   writer.writerows(dists)

