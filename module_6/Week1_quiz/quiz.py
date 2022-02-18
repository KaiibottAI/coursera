#!/usr/bin/env python3

import os
import PIL
from PIL import Image


# Iterate thru all files in the '/images' folder
for file in os.listdir("images"):
    # Iterate thru all the files and ensure they are image files
    try:
        with Image.open(os.path.join("images/", file)) as img:
            # print(os.path.join("images/" + file))
            print(file, img.format, img.size)
            new_img = img.rotate(90).resize((128, 128)).convert("RGB")
            new_img.save(os.path.join("/opt/temp/", file), "JPEG")
    # If file is not an image file, skip file
    except PIL.UnidentifiedImageError:
        # print(f"{file} not an image")
        continue

# Save to the '/opt/icons' directory for all new images
print(os.listdir("/opt/temp/"))
