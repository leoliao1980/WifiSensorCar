# Author: Leo_HC, Liao
# Usage: Ultrasonic sensor library
# Version: 0.1 beta, 06-20-2016

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#TRIG = 23 
#ECHO = 17

def setTrigPin (pin):
  global TRIG
  TRIG = pin
  print "  HC-SR04 TRIG pin is GPIO:", TRIG

def setEchoPin (pin):
  global ECHO
  ECHO = pin
  print "  HC-SR04 ECHO pin is GPIO:", ECHO

#print "Distance Measurement In Progress"
def getDistance ():
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

  GPIO.output(TRIG, False)
  #print "Waiting For Sensor To Settle"
  time.sleep(2)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)

  #print "Distance:",distance,"cm"
  return distance
