#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT

#Pin Setup
#ldr == light dependant resistor
ldr=24
fan_forward = 20
soil_moisture = 21
water_pump = 16
vent_servo = 02
vent_angle = 90
dht_pin = 19

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_forward, GPIO.OUT)
GPIO.setup(water_pump, GPIO.OUT)
GPIO.setup(soil_moisture, GPIO.IN)
GPIO.setup(vent_servo, GPIO.OUT)



class GreenhouseSystem(object):

	def __init__(self):
		#database definitions could be inserted here
		pass

	soil_moisture_state = GPIO.input(soil_moisture)

	def get_temperature(self):
		humidity, temperature = Adafruit_DHT.read_retry(
			pin = dht_pin,
			retries=5
		)
		return temperature

	def get_humidity(self):
		humidity, temperature = Adafruit_DHT.read_retry(
			pin = dht_pin,
			retries=5
		)
		return humidity

	def ldr_reading(self):
		count=0

		GPIO.setup(ldr, GPIO.OUT)
		GPIO.output(ldr, GPIO.LOW)
		time.sleep(1)

		GPIO.setup(ldr,GPIO.IN)

		while(GPIO.input(ldr)==GPIO.LOW):
			count += 1

		return count

	def open_vent(self, angle = vent_angle):
		#setup pwm on servo pin
		pwm = GPIO.PWM(vent_servo, 50)
		
		#start with 0 duty cycle
		pwm.start(0)

		#Calculate duty cycle
		duty = (angle / 18) + 2
		GPIO.output(vent_servo, True)

		pwm.ChangeDutyCycle(duty)
		sleep(1)

		GPIO.output(vent_servo, False)
		pwm.ChangeDutyCycle(0)

	def record_sensor_values(self):
        """
        Save sensor readings to database
        """
      	pass

    def export_to_csv(self, file_path='/home/pi/greenhouse.csv'):
        """
        Export sensor data from database and save as CSV file in file_path
        Defaults to /home/pi/greenhouse.csv
        """
        pass

def main():
    greenhouse = GreenhouseSystem()

    print("Temperature:")
    print(GreenhouseSystem.get_temperature())
    print("Humidity:")
    print(GreenhouseSystem.get_humidity())
    print("Soil:")
    print(GreenhouseSystem.soil_moisture_state)

if __name__ == '__main__':
    main()


