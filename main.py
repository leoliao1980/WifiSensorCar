#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys and append modules path
import sys
sys.path.append("modules")

from flask import Flask, request, render_template
app = Flask(__name__)

import RPi.GPIO as gpio
import time
import socket
import L298NHBridge as HBridge
#import HCSR04 as sonar
import SG90 as servo
import httplib, urllib

# global variable
#speedleft = 0
#speedright = 0
tilt_angle = 2.0
pan_angle = 7.0

# initail the configuration
servo.setServo(19, 7.0)
servo.setServo(26, 2.0)
#sonar.setTrigPin(23)
#sonar.setEchoPin(17)


s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localip=s.getsockname()[0]
print (localip)

params = urllib.urlencode({'field1': 0, 'key':'N04D7QD8NQFZEQ6D'})     # use your API key generated in the thingspeak channels for the value of 'key'
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")                
try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
except:
        print "connection failed"


@app.route('/')
def index():
  return render_template('index.html', ip=localip)


@app.route('/car/<string:action>')
def ctrl(action):
  global tilt_angle
  global pan_angle
  print 'api action: ' + action
  if action == 'forward':
        HBridge.setMotorLeft(1)
        HBridge.setMotorRight(1)
        params = urllib.urlencode({'field1': 1, 'key':'N04D7QD8NQFZEQ6D'})     # use your API key generated in the thingspeak channels for the value of 'key'
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")                
        try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print response.status, response.reason
                data = response.read()
                conn.close()
        except:
                print "connection failed"
  elif action == 'backward':
        HBridge.setMotorLeft(-1)
        HBridge.setMotorRight(-1)
  elif action == 'left':
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(1)
        time.sleep(0.2)
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
  elif action == 'right':
        HBridge.setMotorLeft(1)
        HBridge.setMotorRight(0)
        time.sleep(0.2)
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
  elif action == 'cam_down':
        if (tilt_angle > 2.0):
            tilt_angle = tilt_angle - 1.0
        elif (tilt_angle < 2.0):
              tilt_angle = 2.0
        #print (tilt_angle)
        servo.setServo(26, tilt_angle)
  elif action == 'cam_up':
        if (tilt_angle < 8.0):
            tilt_angle = tilt_angle + 1.0
        elif (tilt_angle < 8.0):
              tilt_angle = 8.0
        #print (tilt_angle)
        servo.setServo(26, tilt_angle)
  elif action == 'cam_left':
        if (pan_angle > 2.5):
            if (pan_angle < 9.0):
                pan_angle = pan_angle - 1.5
            else:
                pan_angle = pan_angle - 2.0
        elif (pan_angle < 2.5):
              pan_angle = 2.5
        #print (pan_angle)
        servo.setServo(19, pan_angle)
  elif action == 'cam_right':
        if (pan_angle < 13.0):
            if (pan_angle < 7.0):
                pan_angle = pan_angle + 1.5
            else:
                pan_angle = pan_angle + 2.0
        elif (pan_angle > 13.0):
              pan_angle = 13.0
        #print (pan_angle)
        servo.setServo(19, pan_angle)
  elif action == 'cam_middle':
        servo.setServo(19, 7.0)
        servo.setServo(26, 2.0)
  else:
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
        params = urllib.urlencode({'field1': 0, 'key':'N04D7QD8NQFZEQ6D'})     # use your API key generated in the thingspeak channels for the value of 'key'
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")                
        try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print response.status, response.reason
                data = response.read()
                conn.close()
        except:
                print "connection failed"

  return ' '


@app.errorhandler(404)
def error404(error):
  return 'Not Found', 404

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
