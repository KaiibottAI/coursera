#!/usr/bin/env python3

import re
import operator
import csv
import sys

log = 'syslog.log'
errorDict = {}
userDict = {}
pattern = r"(INFO|ERROR) ([\w' ]+|[\w'\[\]# ]+) (\(\w+\)|\(\w+\.\w+\))$"

#regex thru the log files to find the log_user,log_type,log_message
with open(log, 'r') as systemlog:
        for line in systemlog:
                logline = re.search(pattern, line)
                log_user = logline.group(3)[1:-1]
                log_type = logline.group(1)
                log_message = logline.group(2)
                #If the log_type is an 'ERROR'
                if log_type == 'ERROR':
                #If the 'ERROR' log_type is not in the errorDict, add the new entry
                        #print('Made it into the if log_type is "ERROR" block')
                        if log_message not in errorDict.keys():
                                errorDict[log_message] = 0
                        errorDict[log_message] += 1
                #If the log_user is not in the userDict, add the new entry
                if log_user not in userDict.keys():
                        userDict[log_user] = {}
                        userDict[log_user]['ERROR'] = 0
                        userDict[log_user]['INFO'] = 0
                #Assuming the top if statements have gone thru, the keys should exist in both userDict and errorDict at this stage.
                if log_type == 'ERROR':
                        userDict[log_user]['ERROR'] += 1
                elif log_type == 'INFO':
                        userDict[log_user]['INFO'] += 1
#Sort the dictionaries as per Coursera guidelines for the quiz
errorDict = sorted(errorDict.items(), key = operator.itemgetter(1), reverse = True)
userDict = sorted(userDict.items())

with open('error_message.csv','w+') as errorFile:
        for entry in errorDict:
                key,value = entry
                errorFile.write(str(key)+','+str(value)+'\n')
with open('user_statistics.csv','w+') as userFile:
        for entry in userDict:
                key,value = entry
                userFile.write(str(key)+','+str(value)+'\n')
