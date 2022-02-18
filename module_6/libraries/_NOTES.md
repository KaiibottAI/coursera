Instructions:

1. Fetching supplier data

```bash
sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
tar xf ~/supplier-data.tar.gz
````


Libraries to study:

1. Working with supplier images

```python
#!/usr/bin/env python3

from PIL import Image
import os, sys

src = "~/supplier-data/images/"

for filename in os.listdir(src):
  path = os.path.join(src, filename)
  if not os.path.isfile(path):
    continue
  try:
    with Image.open(path) as im:
      im = im.convert("RGB")
      im = im.resize((600, 400)).save(path + ".jpeg")
      print("Converting file {} to JPEG".format(path))
  except OSError:
    print("Cannot convert {}".format(path))

```

2. Uploading images to web server

This is an example on the box
```python
#!/usr/bin/env python3

import requests

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
  r = requests.post(url, files={'file': opened})

```

```python
#!/usr/bin/env python3

import requests

url = "IP"
src = "~/supplier-data/images/"

for file in os.listdir(src):
  path = os.path.join(src, file)
  if not os.path.isfile(path):
    continue
  try:
    with open(path, 'rb') as opened:
      r = requests.post(url, files={'file': opened})


```

3. Uploading the descriptions

```python
#!/usr/bin/env python3

import json, requests, os

src = "/home/afk/supplier-data/descriptions"

for file in os.listdir(src):
    path = os.path.join(src, file)

    with open(path) as file_f:
        fruit_file = file_f.readlines()
        fruit_name, fruit_description = fruit_file[0], fruit_file[2]
        fruit_weight = fruit_file[1].replace(" lbs", "")
        fruit_weight = int(fruit_weight)
        # print(fruit_name, fruit_description, fruit_weight)
        jason = {
            "name": fruit_name.strip(),
            "weight": fruit_weight,
            "descrpition": fruit_description.strip(),
            "image_name": "",
        }
```

4. email (constructing email)

5. psutil (processes and system utilization)

6. shutil (file operations)

```python
#!/usr/bin/env python3

import shutil, psutil, socket, os, sys
import emails

def disk_check():
  diskFree = shutil.disk_usage('/')[2] * (1024**3)
  diskTotal = shutil.disk_usage('/')[0] * (1024**3)
  return diskFree <= (diskTotal * .2)

def cpu_check():
  cpuFree = psutil.cpu_percent(interval=0.1)
  return cpuFree <= 0.8

def memory_check():
  memoryFree = psutil.virtual_memory()[1]
  memoryFree = round((memoryFree / (1024**3)), 2)
  return memoryFree <= 0.5

def localhost_check():
  addr = socket.gethostbyname('localhost')
  return addr != "127.0.0.1"
  
if disk_check():
  health_error = "Error - Available disk space is less than 20%"
if  cpu_check():
  health_error = "Error - CPU usage is over 80%"
if memory_check():
  health_error = "Error - Available memory is less than 500MB"
if localhost_check():
  health_error = "Error - localhost cannot be resolved to 127.0.0.1"

```

7. smtplib (sending email)

```python
import smtplib
from email.message import EmailMessage

def send_healthcheck_email()
  s = smtplib.SMTP('localhost')
  msg = EmailMessage()
  msg['To'] = "automation@example.com"
  msg['From'] = "username@example.com"
  msg['Subject'] = healthcheck_email()
  msg.set_content("Please check your system and resolve the issue as soon as possible.")

  if healthcheck:
    s.send_message(msg)
    s.quit()
```