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