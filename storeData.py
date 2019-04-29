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

x = x.replace(' |', '')
print x

data = x.split()
print data[0]

try:
    db = sqlite3.connect('/home/pi/ECE331/datalogger/datalogger.db')

    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")

    temp = db.cursor()
    temp.execute("INSERT INTO pidata(Date, Time, TEMP1, IR, FULL, VIS, LUX, TEMP2, PRESSURE, HUMID) VALUES (?,?,?,?,?,?,?,?,?,?)",(date,time,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

    db.commit()

except sqlite3.Error, e:
    print "Error: %s" % e.args[0]
    sys.exit(1)

    db.close()
