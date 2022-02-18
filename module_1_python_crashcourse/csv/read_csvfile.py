#!/usr/bin/env python3

import csv #import the csv library from python to read thru a csv file

with open('software.csv') as software: #open the csv file 
	reader = csv.DictReader(software) #use csv.DictReader to read thru the lines in the csv file
	for row in reader: #iterate thru the rows in the "reader" of the csv
		print("{} has {} users".format(row["name"],row["users"])) #format the output of the csv to show name and user amount


