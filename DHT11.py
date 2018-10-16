#!/usr/bin/python

import sys
import Adafruit_DHT
from time import sleep

i = 10800

file=open("DHT_Data.txt","w")


while i > 0:
    if i == 10799:
        print("DHT is operating normally")
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    file.write('Temp :{0:0.1f} C Humidity:{1:0.1f} \n'.format(temperature,humidity))
    i=i-1

=======
# This program initializes and records data from the density humidity temperature sensor (DHT11)

# Source website for more information is http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

#Downloads from website needed

import sys
import Adafriut_DHT


i = 500

file=open("DHT_Data.txt","w")

tempArray = []
humidityArray = []

while i > 0:
    humidity, temperature = Adafriut_DHT.read_retry(11,4)
    humidityArray.append(humidity)
    tempArray.append(temperature)
    file.write(str(humidity))
    file.write(str(temperature))
    i=i-1

