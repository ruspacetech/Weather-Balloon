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

