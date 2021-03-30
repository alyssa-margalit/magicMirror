import paho.mqtt.client as mqtt
import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math


sonic = 4
led = 2
button = 3
pinMode(button,"INPUT")
pinMode(led,"OUTPUT")
r = 0
g = 0
b = 0


if __name__ == '__main__':
	setText("hi")
	setRGB(255,0,0)
	b = int(input())
	while True:
		distance = grovepi.ultrasonicRead(sonic)
		dist = int(distance)
		r = dist
		button_status = digitalRead(button)
		if button_status:
			g = g+2
		setRGB(r,g,b)
       


