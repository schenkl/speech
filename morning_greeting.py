#!/usr/bin/python

#this was written for python 2.7 work need to be done to be python3 compatible
#reserrected speak1 to Kent 1/2023 over new year with everyone getting covid
# LUS

import os
import pdb
import socket
import time
from datetime import date
from datetime import datetime
today = date.today()

dt = datetime.now()

# get weekday name
#print('day Name:', dt.strftime('%A'))
#print('month Name:', dt.strftime('%B'))
#print('date:', dt.strftime('%d'))
#print('hour:', dt.strftime('%H'))
#print('min:', dt.strftime('%M'))

Day = dt.strftime('%A')
Hour = dt.strftime('%A')
Month = dt.strftime('%B')
Date = dt.strftime('%d')
Hour = dt.strftime('%H')
Min = dt.strftime('%M')
if Day[0] == '0':
    Day[0] = Day[1]
    Day[1] = 0
if Hour[0] == '0':
    hour = int(Hour)
    Hour = str(hour)

command = "/home/pi/sounds/tts-4.sh  today is " + Day + " " + Month + " " + Date 
#print(command)
os.system(command)


command = "/home/pi/sounds/tts-4.sh  time is now " + Hour + " " + Min
#print(command)
os.system(command)


def get_value(device):
    #pdb.set_trace()
    ip = "192.168.1.122"
    port = 1234
    try:
        #print ("opening connection to 192.168.1.122 port 1234")
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        data = b'R\t' + device + '\n'
        s.send(data)
        #time.sleep(1)
    except:
        print('unable to connect with ruby_server')
    try: 
            msg = s.recv(200)
            if len(msg) == 0:
                return
            else:
                #print("msg: ",msg)
                msgs = msg.split("\n")
		#print(msgs)
                return(msgs[0])
    except:
        print("Fail in get_value")

device = "Sun_rise"
Sun_rise = get_value(device)
device = "Sun_set"
Sun_set = get_value(device)
device = "Kent_ext_temp"
Kent_ext_temp = get_value(device)


#print("Sun_rise = ",Sun_rise)
#print("Sun_set = ",Sun_set)
#print("Kent_ext_temp",Kent_ext_temp)

dark = int(Sun_rise) + ((60*24) - int(Sun_set))
light = (60*24) - dark 
#pdb.set_trace()
light_hours = light / 60
light_minutes = light % 60

sunrise_hour =int(Sun_rise) / 60
sunrise_minutes = int(Sun_rise) % 60
if sunrise_minutes < 10:
    sm = '0' + str(sunrise_minutes)
else:
    sm = str(sunrise_minutes)
sunset_hour = int(Sun_set) / 60;
sunset_minutes = int(Sun_set) % 60
if sunset_minutes < 10:
    ss = '0' + str(sunset_minutes)
else:
    ss = str(sunset_minutes)
#pdb.set_trace()

command = "/home/pi/sounds/tts-4.sh Sun rise is at " + str(sunrise_hour) + " " + sm + " and sun set is at " + str(sunset_hour) + " " + ss
#command = "/home/pi/sounds/tts-4.sh Sun rise is at " + str(sunrise_hour) + " " + str(sunrise_minutes) + " and sun set is at " + str(sunset_hour) + " " + str(sunset_minutes)
os.system(command)

command = "/home/pi/sounds/tts-4.sh There are " + str(light_hours) + " hours " + str(light_minutes) + " minutes of daylight today "
#print(command)
os.system(command)

Current_temperature = get_value("Kent_ext_temp")
if Current_temperature < 110:
    command = "/home/pi/sounds/tts-4.sh current temperature is " + str(Current_temperature) 
    os.system(command)

#pdb.set_trace()
Expected_Rain1 = get_value("Expected_Rain1")
messages = Expected_Rain1.split(";")
Expected_Rain1 = messages[6]
if (Expected_Rain1 > 2):
    Expected_Rain1 = messages[7]
Expected_Rain2 = get_value("Expected_Rain2")
messages = Expected_Rain2.split(";")
Expected_Rain2 = messages[6]
if (Expected_Rain2 > 2):
    Expected_Rain2 = messages[7]
Expected_Min_T = get_value("Expected_Min_T")
messages = Expected_Min_T.split(";")
Expected_Min_T = messages[6]
if ((Expected_Min_T > 120) or (Expected_Min_T < -50)):
    Expected_Min_T = messages[7]
Expected_Max_T = get_value("Expected_Max_T")
messages = Expected_Max_T.split(";")
Expected_Max_T = messages[6]
if ((Expected_Max_T > 120) or (Expected_Max_T < -50)):
    Expected_Max_T = messages[7]
#print(Expected_Max_T)

Expected_Rain1 = Expected_Rain1[:4]
#print("Expected_Rain1 = ",Expected_Rain1)
Expected_Rain1 = Expected_Rain1.replace(".","")
Expected_Rain2 = Expected_Rain2[:4]
Expected_Rain2 = Expected_Rain2.replace(".","")
#print("Expected_Rain2 = ",Expected_Rain2)
Expected_Min_T = Expected_Min_T[:4]
#print("Expected_Min_T = ",Expected_Min_T)
Expected_Max_T = Expected_Max_T[:4]
#print("Expected_Max_T = ",Expected_Max_T)
#pdb.set_trace()

command = "/home/pi/sounds/tts-4.sh the expected high temperature for today is " + str(Expected_Max_T) + " and the expected low temperature is " + str(Expected_Min_T)
#print(command)
os.system(command)

#pdb.set_trace()

#print("Expected_Rain1: ",Expected_Rain1)
#if Expected_Rain1 == "0":
if "000" in Expected_Rain1:
    command = "/home/pi/sounds/tts-4.sh no rain is expected today "
else:
    command = "/home/pi/sounds/tts-4.sh probability of rain today is " + str(Expected_Rain1) + " percent "
os.system(command)

    
mqtt_error = get_value("Mqtt_dev_error")
messages = mqtt_error.split(";")
mqtt_error = messages[6]
#print(mqtt_error)
if mqtt_error == "2":
	command = ("/home/pi/sounds/tts-4.sh there are no M Q T T devices off line")
else :
	command = ("/home/pi/sounds/tts-4.sh there are some  M Q T T devices off line")
os.system(command)
