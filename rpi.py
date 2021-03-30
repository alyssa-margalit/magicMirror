import paho.mqtt.client as mqtt
import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math


sonic = 4
sonic2 = 8
led = 2
button = 3
pinMode(button,"INPUT")
pinMode(led,"OUTPUT")
r = 0
g = 0
b = 0


if __name__ == '__main__':
	setText(" ")
	setRGB(255,0,0)
	#b = int(input())
	while True:
		distance = grovepi.ultrasonicRead(sonic)
		dist = int(distance)
		r = 1 - (dist/500)
		r = r*255
		print("red value: "+ str(r))
		distance2 = grovepi.ultrasonicRead(sonic2)
		dist2 = int(distance2)
		b = 1 - (dist2/500)
		b = b*255
		print("blue value: "+ str(b))
		button_status = digitalRead(button)
		if button_status:
			g = g+2
			print("green value: "+ str(g))
		setRGB(r,g,b)
		setText(str(r)+","+str(g)+","+str(b))
		time.sleep(.3)
       


