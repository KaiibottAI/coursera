#!/usr/bin/env python3

import os
import csv
import random

with open("csv_files\Smash Team.csv", "r") as SmashTeam: #open the smash team csv to get the Names (owners) of the team
    smash_reader = csv.DictReader(SmashTeam)
    with open("csv_files\DraftOrder.txt", "w+") as DraftOrder: #create a DraftOder.txt for future lists
        DraftList = [] #create variable for the list a "DraftList"
        for row in smash_reader: #iterate thru each row in the original csv file
            print("Team Captain is {} representing their Team \"{}\"".format(row["Name"],row["Team"])) #print the Team Captains and their teams
            DraftList.append(row["Name"]) #add the team captains to the draft list
        random.shuffle(DraftList) #shuffle the Draft list
        for ii,CaptainName in enumerate(DraftList): #for each name (ii) in the Draft List, export to the DraftOrder.txt for keeping
            DraftOrder.write(str(CaptainName) + "\n")
        print("The Draft will be in the following order: " + "\n")
        for index, CaptainNames in enumerate(DraftList): #for index (position) and CaptainNames from enumerated List of DraftList
            print("{} - {}".format(index + 1, CaptainNames)) #write the postion of the teams in the console
