#!/usr/bin/python

import sys
import sqlite3
import datetime
import time
import serial

ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=None)

ser.write('Give\n')

x=ser.readline()
print x



#TEMP1 = sys.argv[1]
#IR = sys.argv[2]
#FULL = sys.argv[3]
#VIS = sys.argv[4]
#LUX = sys.argv[5]
#TEMP2 = sys.argv[6]
#PRESSURE = sys.argv[7]
#HUMID = sys.argv[8]


