# ECE331 Project 2 Datalogger
 The storeData.py script is used to recieve data from the piHat and store it into an sqlite3 Database. This code works properly and is 
 executed every minute using cron.
 
 getData.php is a php script that is called by index.html. This script gets the last 24 hours worth of data from the sqlite database and
 puts it into a json format so it can be read and plotted using ChartJS. 
 
 Unfortunately I began going in a different plotting method (as can be seen in the file graphdata.py) where instead of using ChartJS I was
 going to use plot.ly to make very clean and more interactive plots. I ran into a lot of errors and this ended up taking up way too much of 
 my time. Because of this is ran out of time to figure out the ChartJS scripts to make a chart for all of the data. A website is still up 
 on the public internet and it currently displaying sample data. 
 
 datalogger.db is the database that holds the piHat data and datalogger.pl is a pearl script originally intended to do the job of storeData.py
 and collect the piHat data and store it, but problems with perl made me decide to use python instead. 
 
 create_table is just a file to easily make a new table in sqlite3 using .read
 
 lighttpd server is successfully installed and runs at boot. 

