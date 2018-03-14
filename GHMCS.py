#GREENHOUSE MONITORING AND CONTROL SYSTEM 

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

#Code for the soil moisture sensor

#Code for the LDR
def RCtime (RCpin)
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(RCPin, GPIO.IN)

	while (GPIO.input(RCpin)==GPIO.LOW):
		reading +=1

	return reading

while True:
	print RCtime(21)




