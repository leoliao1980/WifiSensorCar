#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys and append modules path
import sys
sys.path.append("modules")

from flask import Flask, request, render_template
app = Flask(__name__)

import RPi.GPIO as gpio
import time
import L298NHBridge as HBridge
import socket

#speedleft = 1
#speedright = 1

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localip=s.getsockname()[0]
print (localip)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/car/<string:action>')
def ctrl(action):
  print 'api action: ' + action
  if action == 'forward':
		HBridge.setMotorLeft(1)
		HBridge.setMotorRight(1)
  elif action == 'backward':
		HBridge.setMotorLeft(-1)
		HBridge.setMotorRight(-1)
  elif action == 'left':
		HBridge.setMotorLeft(0)
		HBridge.setMotorRight(1)
  elif action == 'right':
		HBridge.setMotorLeft(1)
		HBridge.setMotorRight(0)
  else:
		HBridge.setMotorLeft(0)
		HBridge.setMotorRight(0)
    
  return ' '


@app.errorhandler(404)
def error404(error):
  return 'Not Found', 404

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
