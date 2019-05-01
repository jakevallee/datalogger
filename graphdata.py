#!/usr/bin/python

#This script was for plotting the data with plot.ly but this ended up bring
#harder than i expected and used up a lot of my time. Doesn't work

#Import dependencies
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import sqlite3
import pandas as pd
import time
import datetime
from datetime import datetime as dt

#Connect to the database
db = sqlite3.connect('/home/pi/ECE331/datalogger/datalogger.db')

#Create a cursor to enable editing
cursor = db.cursor()
cursor.execute('SELECT * FROM pidata DESC LIMIT 1400')

rows = cursor.fetchall()
str(rows)

df = pd.DataFrame([[ij for ij in i] for i in rows])

df.rename(columns={0: 'Date', 1: 'Time', 2: 'TEMP1', 3: 'IR', 4: 'FULL', 5: 'VIS', 6: 'LUX', 7: 'TEMP2', 8: 'PRESSURE', 9: 'HUMID'}, inplace=True);

#Settup each plot
temp = go.Scatter(
        x=df['Time'],
        y=df['TEMP1'],
        name='Temp 1'
        )

IR = go.Scatter(
        x=df['Time'],
        y=df['IR'],
        name='IR'
        )
 

FULL = go.Scatter(
        x=df['Time'],
        y=df['FULL'],
        name='Temp 1'
        )

VIS = go.Scatter(
        x=df['Time'],
        y=df['VIS'],
        name='Temp 1'
        )

LUX = go.Scatter(
        x=df['Time'],
        y=df['LUX'],
        name='Temp 1'
        )

temp2 = go.Scatter(
        x=df['Time'],
        y=df['TEMP2'],
        name='Temp 1'
        )

pressure = go.Scatter(
        x=df['Time'],
        y=df['PRESSURE'],
        name='Temp 1'
        )

humid = go.Scatter(
        x=df['Time'],
        y=df['HUMID'],
        name='Temp 1'
        )

#Configure the plots

fig = tools.make_subplots(rows = 8, cols = 1, subplot_titles = ('Temperature v Time','IR v. Time','FULL v. Time','VIS v. Time','LUX v. Time','Temperature2 v. Time','Pressure v. Time','HUMID v. Time'))
fig.append_trace(temp,1,1)
fig.append_trace(IR,2,1)
fig.append_trace(FULL,3,1)
fig.append_trace(VIS,4,1)
fig.append_trace(LUX,5,1)
fig.append_trace(temp2,6,1)
fig.append_trace(pressure,7,1)
fig.append_trace(humid,8,1)

fig['layout']['xaxis1'].update(title = 'Time')
fig['layout']['xaxis2'].update(title = 'Time')
fig['layout']['xaxis3'].update(title = 'Time')
fig['layout']['xaxis4'].update(title = 'Time')
fig['layout']['xaxis5'].update(title = 'Time')
fig['layout']['xaxis6'].update(title = 'Time')
fig['layout']['xaxis7'].update(title = 'Time')
fig['layout']['xaxis8'].update(title = 'Time')


fig['layout']['yaxis1'].update(title = 'Time')
fig['layout']['yaxis2'].update(title = 'Time')
fig['layout']['yaxis3'].update(title = 'Time')
fig['layout']['yaxis4'].update(title = 'Time')
fig['layout']['yaxis5'].update(title = 'Time')
fig['layout']['yaxis6'].update(title = 'Time')
fig['layout']['yaxis7'].update(title = 'Time')
fig['layout']['yaxis8'].update(title = 'Time')

fig['layout'].update(title = 'Weather Station Data')

#Plot
py.iplot(fig, filename='sensorplots.html')
