#!/usr/bin/env python3

#import the necessary modules for this project
import os
import csv
import random

#Create the Roster of players. Name, Team and future Roster to hold character names.
names = [ {"Name": "Zenyeezus", "Team": "God and Anime", "Roster": " "},
{"Name": "RZ", "Team": "B", "Roster": " "}, 
{"Name": "AFKMusiic", "Team": "NOOB", "Roster": " "}, 
{"Name": "Fishinator42", "Team": "D", "Roster": " "}, 
{"Name": "Youre A Squid Youre A Kid", "Team": "E", "Roster": " "},
{"Name": "Narwhal", "Team": "F", "Roster": " "} ]

#Define the keys for the csv dictionary for later use
keys = ["Name", "Team", "Roster"]

#open/create the file for the smash teams.
with open("csv_files\Smash Team.csv", "w+") as SmashTeam:
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    writer = csv.DictWriter(SmashTeam, fieldnames = keys) #csv.DictWriter adds the fieldname Keys to the top of SmashTeam
    writer.writeheader() #write header
    writer.writerows(names) #write the values of the rows

