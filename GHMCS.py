#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
#GPIO SETUP
fan_forward = 20
soil_moisture = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_forward, GPIO.OUT)
GPIO.setup(soil_moisture, GPIO.IN)
#infinite loop
while True:
	print "Hello world"

	humidity, temperature = Adafruit_DHT.read_retry(11,4)

	print "Temperature: " + str(temperature) + " C"
	print "Humidity: " + str(humidity) + " %%"

	soil_moisture_state = GPIO.input(soil_moisture)

	if (soil_moisture_state == 1):
		print "Soil State is 1"
		GPIO.output(fan_forward, GPIO.HIGH)
	else:
		print "Soil State is 0"
		GPIO.output(fan_forward, GPIO.LOW)


	sleep(2)


