#!/usr/bin/python3


#also daemon that speaks alerts sent from pi-2 send over port 3333
#Feb 9, 2020 Starlight, making maple syrup while Maura is in California
#taking Holotrophic Breath Works course

# import socket programming library 
import socket 

# import thread module 
from _thread import *
import threading 
import pdb
import os

print_lock = threading.Lock() 

# thread function 
def threaded(c): 
	while True: 
		file_num = ''
		file_num = c.recv(1024) 
		print("file_num raw: ",file_num)
		#pdb.set_trace()
		try:
			if len(file_num) > 1: 
				int.from_bytes(file_num, byteorder='big')
				#file_num = file_num.decode()
				file_num = int(file_num)
			else:
				print('Bye') 
				# lock released on exit 
				print_lock.release() 
				break
		except:
			print('Unable to convert file_num into a int')
			#c.close()
			#break
			print('Setting file_num to -1')
			file_num = -1
		print('file_num = :',file_num)
		#pdb.set_trace()
		#if not file_num: 
		try:
			if file_num > 0:
				rtn = play_warning(file_num)
		except:
			print('unable to call play_warning')

	# connection closed 
	c.close() 

def play_warning(file_num):
	print('play_warning: file_num: ',file_num)
	try:
		if file_num == 1:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/1")
		elif file_num == 2:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/2")
		elif file_num == 3:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/3")
		elif file_num == 4:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/4")
		elif file_num == 5:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/5")
		elif file_num == 6:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/6")
		elif file_num == 7:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/7")
		elif file_num == 8:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/8")
		elif file_num == 9:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/9")
		elif file_num == 10:
			os.system("/usr/bin/aplay /home/pi/sounds/speech/10")
		elif file_num == 11:
                        os.system("/usr/bin/aplay /home/pi/sounds/speech/11")
		elif file_num == 12:
                        os.system("/usr/bin/aplay /home/pi/sounds/speech/12")
		else:
			print('Sorry, no file by that name')
	except:
		print('unable to play sound file')



def Main(): 
	host = "" 
	port = 3333
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 
	# put the socket into listening mode 
	s.listen(5) 
	print("socket is listening") 
	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		c, addr = s.accept() 
		# lock acquired by client 
		print_lock.acquire() 
		print('Connection from:', addr[0], ':', addr[1]) 
		start_new_thread(threaded, (c,)) 
	s.close() 


if __name__ == '__main__': 
	Main() 

