#!/usr/bin/env python3

import csv

users = [{"Name": "Sol Mansi", "Username": "solm", "Department": "IT Infrastructure"}, {"Name": "Lio Nelson", "Username": "lion", "Department": "User Experience Research"}, {"Name": "CHarlie Grey", "Username": "greyc", "Department": "Development"}]
keys = ["Name","Username","Department"]
#users = the dictionary values
#keys = the keys of the dictionary
with open('by_department.csv', 'w') as by_department: #create/open a csv file for writing
     writer = csv.DictWriter(by_department, fieldnames = keys) #opens the "DictWriter" to pass the keys. the "fieldnames" parameter is the keys.
     writer.writeheader() #writeheader will write the first line as the keys
     writer.writerows(users) #writerows will write the dictionary values