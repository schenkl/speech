#!/usr/bin/python

#hm	hour	min
#Sun_rise
#Kent_ext_temp
#Sun_set

import os
import pdb
import socket
import time
from datetime import date
from datetime import datetime
today = date.today()

dt = datetime.now()

# get weekday name
print('day Name:', dt.strftime('%A'))
print('month Name:', dt.strftime('%B'))
print('date:', dt.strftime('%d'))
print('hour:', dt.strftime('%H'))
print('min:', dt.strftime('%M'))

Day = dt.strftime('%A')
Hour = dt.strftime('%A')
Month = dt.strftime('%B')
Date = dt.strftime('%d')
Hour = dt.strftime('%H')
Min = dt.strftime('%M')
if Day[0] == '0':
    Day[0] = Day[1]
    Day[1] = 0

command = "/home/pi/sounds/tts-4.sh  today is " + Day + " " + Month + " " + Date 
print(command)
os.system(command)


command = "/home/pi/sounds/tts-4.sh  time is now " + Hour + " " + Min
print(command)
os.system(command)


def get_value(device):
    #pdb.set_trace()
    ip = "192.168.1.122"
    port = 1234
    try:
        print ("opening connection to 192.168.1.122 port 1234")
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
                print("msg: ",msg)
		msgs = msg.split("\n")
		print(msgs)
		return(msgs[0])
    except:
        print("Fail in get_value")

device = "Sun_rise"
Sun_rise = get_value(device)
device = "Sun_set"
Sun_set = get_value(device)
device = "Kent_ext_temp"
Kent_ext_temp = get_value(device)


print("Sun_rise = ",Sun_rise)
print("Sun_set = ",Sun_set)
print("Kent_ext_temp",Kent_ext_temp)

dark = int(Sun_rise) + ((60*24) - int(Sun_set))
light = (60*24) - dark 
#pdb.set_trace()
light_hours = light / 60
light_minutes = light % 60

command = "/home/pi/sounds/tts-4.sh There are " + str(light_hours) + " hours " + str(light_minutes) + " minutes of daylight today "
print(command)
os.system(command)

