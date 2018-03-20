#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT

#Pin Setup
fan_forward = 20
soil_moisture = 21
water_pump = 16
vent_servo = 02
#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_forward, GPIO.OUT)
GPIO.setup(water_pump, GPIO.OUT)
GPIO.setup(soil_moisture, GPIO.IN)


#infinite loop
while True:
	print "Hello world"

	humidity, temperature = Adafruit_DHT.read_retry(11,4)

	print "Temperature: " + str(temperature) + " C"
	print "Humidity: " + str(humidity) + " %%"

	soil_moisture_state = GPIO.input(soil_moisture)

	if (soil_moisture_state == 1):
		print "The soil is dry"
		GPIO.output(water_pump, GPIO.HIGH)
		sleep(3)
	else:
		print "The soil is wet"
		GPIO.output(water_pump, GPIO.LOW)

	if (temperature > 29):
		print "High Temperature, starting fan"
		GPIO.output(fan_forward, GPIO.HIGH)

		open_vent()


	sleep(2)

#function to open vent
def open_vent():

	pass

