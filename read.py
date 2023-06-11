import serial 
import time 
import sys
import struct
import subprocess
import os

port = '/dev/serial0'

baudrate = 115200 

ser = serial.Serial(port,baudrate,timeout=1)


def send_temperature():
	os.chdir("/home/satlla0/Desktop/scripts/")
	subprocess.run(["python","temperature.py"])
	return True
	
def send_take_a_picture():
	os.chdir("/home/satlla0/Desktop/scripts/")
	subprocess.run(["python","take_a_picture.py"])
	return True
	
def send_compress_image():
	os.chdir("/home/satlla0/Desktop/scripts/")
	subprocess.run(["python","compress_and_send.py"])
	photo_file = '/home/satlla0/Desktop/scripts/0.jpg'
	with open(photo_file,'rb') as file:
		photo_data = file.read()
		ser.write(photo_data)
	return True
			
data = ""		

if __name__ == '__main__':
	while True:
		try:
			if not ser.is_open:
				print("failed open serial port")
				sys.exit(1)
			else:
				if ser.in_waiting > 0:
					try:
						data = ser.readline().decode()
					except serial.SerialException as e:
						print("serial port error ",str(e))
				if "temperature" in data:
					send_temperature()
				elif "take picture" in data:
					send_take_a_picture()
				elif "compress image" in data:
					send_compress_image()
				elif "to send" or "done..." in data:
					continue
				if len(data) > 3:
					print("received ",data)
			
			
		except serial.SerialException as e:
			print("serial port error ",str(e))
			sys.exit(1)
			
	ser.close()
