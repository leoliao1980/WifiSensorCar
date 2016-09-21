# Author: Leo_HC, Liao
# Usage: Servo SG90 library
# Version: 0.1 beta, 06-28-2016

import RPi.GPIO as GPIO
import time
import os

def setServo(pin, degrees):
        # GPIO.setwarnings(False)
        # Set the layout for the pin declaration
        GPIO.setmode(GPIO.BCM)
        # The pin is the out pin for the PWM signal for the servo.
        GPIO.setup(pin, GPIO.OUT)

	# Now we will start with a PWM signal at 50Hz. 
	# 50Hz should work for many servos very will.
	# If not you can play with the frequency if you like.
	Servo = GPIO.PWM(pin, 50)						

	# This command sets the left position of the servo
	Servo.start(2.5)

	# You can play with the values.
	# 7.5 is in most cases the middle position
	# 12.5 is the value for a 180 degree move to the right
	# 2.5 is the value for a -90 degree move to the left
	#print "move to the %% position:"
	Servo.ChangeDutyCycle(degrees)
	time.sleep(1)


def stopServod():
    os._exit(1)
    Servo.stop()
    GPIO.cleanup()

