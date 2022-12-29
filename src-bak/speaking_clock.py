#!/usr/bin/python3

#clock that rings chimes every i5 minutes
#from schedule defined/uploadable

#also daemon that speaks alerts sent from pi-2 send over port
#Feb 9, 2020 Starlight, making maple syrup while Maura is in California
#taking Holotrophic Breath Works course

import time                    # This clock works with RasPiO InsPiRing Circle
from time import sleep         # http://rasp.io/inspiring
#from datetime import datetime
import datetime
import threading
import socket
import pdb
import sys
import os

old_hour = -1
old_minute = -1
old_quarter = -1
start_hour = 6
end_hour = 20

def hour_ring():
	print('New Hour')
	os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hour-chime.wav")

def hour_chime(hour):
	print('ringing hour  ',hour)
	if hour > 12:
		hour = hour - 12
	if hour == 1:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-1.wav")
	if hour == 2:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-2.wav")
	if hour == 3:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-3.wav")
	if hour == 4:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-4.wav")
	if hour == 5:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-5.wav")
	if hour == 6:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-6.wav")
	if hour == 7:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-7.wav")
	if hour == 8:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-8.wav")
	if hour == 9:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-9.wav")
	if hour == 10:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-10.wav")
	if hour == 11:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-11.wav")
	if hour == 12:
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/Hours-12.wav")

def quarter_hour(quarter):
	print('ringing quarter hour  ',quarter)
	if quarter == 1:
		#os.system("/usr/bin/aplay /home/pi/sounds/chimes/Quarter-hour-1.wav")
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/MiddlePitchChime-1.wav")
	if quarter == 2:
		#os.system("/usr/bin/aplay /home/pi/sounds/chimes/Quarter-hour-2.wav")
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/MiddlePitchChime-2.wav")
	if quarter == 3:
		#os.system("/usr/bin/aplay /home/pi/sounds/chimes/Quarter-hour-3.wav")
		os.system("/usr/bin/aplay /home/pi/sounds/chimes/MiddlePitchChime-3.wav")

def main():
	global hour,quarter,old_hour,old_minute,old_quarter
	while True:
		now = datetime.datetime.now()
		print ( now.year, now.month, now.day, now.hour, now.minute, now.second)
		hour = now.hour
		minute = now.minute
		second = now.second
		if (hour < start_hour) or (hour > end_hour):
			print('hour out of range...quiet time')
		else:
			quarter = int(minute/15)
			if old_hour != hour:
				hour_ring()
				old_hour = hour
			if quarter != old_quarter:
				hour_chime(hour)
				quarter_hour(quarter)
				old_quarter = quarter
				old_hour = hour

		time.sleep(5)
main()
