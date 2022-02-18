#!/usr/bin/env python3

"""
Putting all the health checks together with own email def
"""

import shutil, psutil, socket, os, sys
import smtplib
from email.message import EmailMessage

# Check if Disk free space is more than 80%
def disk_check():
    diskFree = shutil.disk_usage("/")[2] * (1024**3)
    diskTotal = shutil.disk_usage("/")[0] * (1024**3)
    return diskFree <= (diskTotal * 0.2)


# Check if CPU is higher than 80% usage
def cpu_check():
    cpuFree = psutil.cpu_percent(interval=0.1)
    return cpuFree <= 0.8


# Check if Memory is less than 500 MB free
def memory_check():
    memoryFree = psutil.virtual_memory()[1]
    memoryFree = round((memoryFree / (1024**3)), 2)
    return memoryFree <= 0.5


# Check if localhost resolves back to 127.0.0.1
def localhost_check():
    addr = socket.gethostbyname("localhost")
    return addr != "127.0.0.1"


# Send an email about an error
def health_email(health_status):
    msg = EmailMessage()
    msg["From"] = "automation@example.com"
    msg["To"] = "{}@example.com".format(os.environ["USER"])
    msg["Subject"] = health_status
    msg.set_content(
        "Please check your system and resolve the issue as soon as possible."
    )

    s = smtplib.SMTP("localhost")
    # s.send_message(msg)
    s.quit


# If any of the above return True, generate the error message of what is wrong and send an email
if disk_check():
    health_error = "Error - Available disk space is less than 20%"
    health_email(health_error)
if cpu_check():
    health_error = "Error - CPU usage is over 80%"
    health_email(health_error)
if memory_check():
    health_error = "Error - Available memory is less than 500MB"
    health_email(health_error)
if localhost_check():
    health_error = "Error - localhost cannot be resolved to 127.0.0.1"
    health_email(health_error)
