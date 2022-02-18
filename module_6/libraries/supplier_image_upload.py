#!/usr/bin/env python3

import requests

url = "http://localhost/upload"
src = "supplier-data/images/"

fruit_pics = os.listdir(src)

for fruit in fruit_pics:
    if fruit.endswith(".jpeg"):
        with open(src + fruit, "rb") as opened:
            r = requests.post(url, files={"file": opened})


#!/usr/bin/env python3
import os, sys
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"

images = os.listdir(path)

for image in images:
    if image.endswith(".jpeg"):
        with open(path + image, "rb") as opened:
            r = requests.post(url, files={"file": opened})
