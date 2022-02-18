#!/usr/bin/env python3

from PIL import Image
import os, sys

src = "supplier-data/images/"

images = os.listdir(src)

for image in images:
    if ".tiff" in image:
        image_name = os.path.splitext(image)[0]
        new_name = src + image_name + ".jpeg"
        try:
            with Image.open(src + image) as im:
                im = im.convert("RGB").resize((600, 400)).save(new_name)
                print("Converting file {} to JPEG".format(src + image))
        except OSError:
            print("Cannot convert {}".format(src + image))
