#!/usr/bin/perl


use Device::SerialPort qw( :PARAM :STAT 0.07 );
use strict;
use warnings;
use DBI;

my $dbh = DBI->connect("dbi:SQLite3:dbname=datalogger.pl","","")
        or die $DBI::errstr;


my $port = Device::SerialPort->new("/dev/ttyACM0");

#Connected to database and serial Port


$port->write("Give me the data\n");

my $mydata = "";
until ($mydata ne "") {
        $mydata = $port->lookfor; #Poll until data received
        die "No data collected\n" unless (defined $mydata);
        sleep .5;
}

# printf "%s\n", $mydata;

$mydata =~ s/\|/ /g;
$mydata =~ s/ +/ /g;
printf "%s\n", $mydata;

my @data = split / /, $mydata;
printf("%s\n", @data);

my $command = qq(INSERT INTO pidata(DateTime,TEMP1,IR,FULL,VIS,LUX,TEMP2,PRESSURE,HUMID) VALUES(datetime('now'),$data[0],$data[1],$data[2],$data[3],$data[4],$data[5],$data[6],$data[7]));

printf("About to update\n");
$dbh->do($command) or die "Error exec\n";
printf("Database Updated\n");
