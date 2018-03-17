#!/bin/bash
echo 'UDS Sensor Initializing'
python piUDS.py &
echo 'UDS Sensor Initialized'
echo 'DHT11 Sensor Initializing'
python DHT11.py &
echo 'DHT11 Sensor Initialized'
echo 'Light Sensor Initializing'
python lightResistor.py &
echo 'Light Sensor Initialized'
echo 'MPU6050 Initializing'
python MPU6050.py &
echo 'MPU6050 Initialized'
echo 'Camera Initializing'
python piCamera.py 
echo 'All programs are completed'
