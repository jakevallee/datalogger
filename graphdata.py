import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import sqlite3
import pandas as pd
import time
import datetime
from datetime import datetime as dt

db = sqlite3.connect('/home/pi/ECE331/datalogger/datalogger.db')

cursor = db.cursor()
cursor.execute('SELECT * FROM pidata DESC LIMIT 1400');

rows = cursor.fetchall()
str(rows)

df = pd.DataFrame([[ij for ij in i] for i in rows])
