import RPi.GPIO as GPIO, time, os      
from time import sleep 
DEBUG = 1
GPIO.setmode(GPIO.BCM)
file = open("Light_Data.txt","w")
i=10800 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
 
while i>0:
	if i == 10799:
		print("Light Sensor is operating normally")                                     
        file.write(repr(RCtime(18))+'\n')
	i=i-1


