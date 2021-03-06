#!/usr/bin/python

#This script connects to the piHat via serial and takes that data and stores it
#in a sqlite3 database for it to then later be accessed and used by the ChartJS
#script

import sys
import sqlite3
import datetime
import time
import serial

#Connect serial device
ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=None)

ser.write('Give\n')

x=ser.readline()
# print x

x = x.replace(' |', '')
# print x

data = x.split()
# print data[0]
# Scale the values that need to be scaled
data[5] = float(data[5])/100.0
data[6] = float(data[6])/10000.0
data[7] = float(data[7])/1000.0

try:
    db = sqlite3.connect('/home/pi/ECE331/datalogger/datalogger.db')

    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")
    
    #Insert data from piHat into database 
    temp = db.cursor()
    temp.execute("INSERT INTO pidata(Date, Time, TEMP1, IR, FULL, VIS, LUX, TEMP2, PRESSURE, HUMID) VALUES (?,?,?,?,?,?,?,?,?,?)",(date,time,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))

    db.commit()

except sqlite3.Error, e:
    print "Error: %s" % e.args[0]
    sys.exit(1)

    db.close()
