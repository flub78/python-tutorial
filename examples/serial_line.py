#!/usr/bin/python
# -*- coding:utf8 -*
import serial

import sys

print ("Serial line\n")
# ser = serial.Serial('/dev/ttyUSB0')
ser = serial.Serial('COM3', 9600, timeout=0)



print ("version: ", sys.version_info)
print ("bye")

