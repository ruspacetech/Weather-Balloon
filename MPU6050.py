<<<<<<< HEAD
#!/usr/bin/python

import smbus
import math
from time import sleep
i = 10800
# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

t = 600
def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command
file=open("MPU6050_Data.txt","w")
# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)
while i>0:
	file.write( "gyro data \n")
	file.write( "--------- \n ")

	gyro_xout = read_word_2c(0x43)
	gyro_yout = read_word_2c(0x45)
	gyro_zout = read_word_2c(0x47)
	gyro_xout_scaled = gyro_xout / 131
	gyro_yout_scaled = gyro_yout / 131
	gyro_zout_scaled = gyro_zout / 131
	#file.write(print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131))
	file.write("gyro_xout:")
	file.write(repr(gyro_xout)+'\n')
	file.write('scaled:' +repr(gyro_xout_scaled)+'\n')
	file.write('gyro_yout:' +repr(gyro_yout)+'\n')
	file.write('scaled:' +repr(gyro_yout_scaled)+ '\n')
	file.write('gyro_zout:' +repr(gyro_zout)+'\n')
	file.write('scaled: ' +repr(gyro_zout_scaled)+'\n')

	#file.write(print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131))
	#file.write(print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131))

	#print
	#file.write(print "accelerometer data")
	#file.write(print "------------------")
	file.write("Accelerometer Data \n")
	file.write("----------------- \n")

	accel_xout = read_word_2c(0x3b)
	accel_yout = read_word_2c(0x3d)
	accel_zout = read_word_2c(0x3f)

	accel_xout_scaled = accel_xout / 16384.0
	accel_yout_scaled = accel_yout / 16384.0
	accel_zout_scaled = accel_zout / 16384.0

	#file.write(print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
	file.write('accel_xout:' +repr(accel_xout)+'\n')
	file.write('scaled:' +repr(accel_xout_scaled)+'\n')
	file.write('accel_yout:' +repr(accel_yout)+'\n')
	file.write('scaled:' +repr(accel_yout_scaled)+'\n')
	file.write('accel_zout:' +repr(accel_zout)+'\n')
	file.write('scaled:' +repr(accel_zout_scaled)+'\n')
	#file.write(print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
	#file.write(print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)
	x_rot = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
	y_rot = get_y_rotation(accel_yout_scaled, accel_yout_scaled, accel_zout_scaled)

	file.write('X Rotation:' +repr(x_rot)+'\n')
	file.write('Y Rotation:' +repr(y_rot)+'\n')
	
	#file.write(print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
	#file.write(print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
	sleep(1)
	i= i-1
	if i==10799:
		print("MPU6050 is operating normally")
=======
#Programming for the MPU6050 on the raspberry pi

#This code utilizes the mpu6050-raspberrypi module in order to simplify and streamline the code

#Source website is https://pypi.python.org/pypi/mpu6050-raspberrypi/

#Downloads from website needed
from mpu6050 import mpu6050
accelArray = []
gyroArray = []

i = 500
sensor = mpu6050(0x68)
print("MPU6050 initialized")
while i > 0:
    temp_accel = sensor.get_accel_data()
    temp_gyro = sensor.get_gyro_data()
    accelArray.append(temp_accel)
    gyroArray.append(temp_gyro)
    i = i - 1
print("MPU6050 disabled")
>>>>>>> a1aee89930f986b5c071ab1123635b2a219e54f2
