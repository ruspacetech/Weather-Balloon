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
