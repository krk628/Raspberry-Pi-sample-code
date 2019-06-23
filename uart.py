#!/usr/bin/python

import serial
import sys
import time
import string 
from serial import SerialException

def read_line():
	"""
	taken from the ftdi library and modified to 
	use the ezo line separator "\r"
	"""
	lsl = len('\r')
	line_buffer = []
	while True:
		next_char = ser.read(1)
		if next_char == '':
			break
		line_buffer.append(next_char)
		if (len(line_buffer) >= lsl and
				line_buffer[-lsl:] == list('\r')):
			break
	return ''.join(line_buffer)
	
def read_lines():
	"""
	also taken from ftdi lib to work with modified readline function
	"""
	lines = []
	try:
		while True:
			line = read_line()
			if not line:
				break
				ser.flush_input()
			lines.append(line)
		return lines
	
	except SerialException as e:
		print( "Error, ", e)
		return None	

def send_cmd(cmd):
	"""
	Send command to the Atlas Sensor.
	Before sending, add Carriage Return at the end of the command.
	:param cmd:
	:return:
	"""
	buf = cmd + "\r"     	# add carriage return
	try:
		ser.write(buf.encode('utf-8'))
		return True
	except SerialException as e:
		print ("Error, ", e)
		return None
			
if __name__ == "__main__":
	
	real_raw_input = vars(__builtins__).get('raw_input', input) # used to find the correct function for python2/3
	
	usbport = '/dev/ttyAMA0' # change to match your pi's setup 

        try:
                ser = serial.Serial(usbport, 9600, timeout=0)
        except serial.SerialException as e:
                print "Error, ", e
                sys.exit(0)

#       send_cmd("RT,26.6667")
        send_cmd("R")
        time.sleep(1.3)
        lines = read_lines()
        print lines[0]

