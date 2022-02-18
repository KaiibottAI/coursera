#!/bin/bash

> ErrorLogsFromSyslog.txt
> InfoLogsFromSyslog.txt
> WarningLogsFromSyslog.txt
file=/var/log/syslog

#this will GREP (Global Regular Expression Parser) the word "INFO" from the $file (syslog) and append to the specified file
grep -i "info" $file | cut -d' ' -f6- >> InfoLogsFromSyslog.txt
grep -i "ERROR" $file | cut -d' ' -f6- >> ErrorLogsFromSyslog.txt
grep -i "WARNING" $file | cut -d' ' -f6-  >> WarningLogsFromSyslog.txt