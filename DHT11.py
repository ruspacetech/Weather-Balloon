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