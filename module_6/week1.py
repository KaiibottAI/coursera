#!/usr/bin/env python3

from PIL import Image
import os
from pathlib import Path
import shutil

for file in os.listdir():
    if file.endswith(".png"):
        # print(os.path.abspath(file))
        new_file = file.replace(".png", ".jpg")
        # print(file, new_file)
        with Image.open(file) as im:
            new_im = im.convert("RGB").rotate(180).resize((128, 128))
            new_im.save(new_file)


"""
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'/home/student-01-c288566d918f'
>>> str(Path(os.getcwd()).parents[1])
'/'
>>> str(Path(os.getcwd()).parents[2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/pathlib.py", line 594, in __getitem__
    raise IndexError(idx)
IndexError: 2
>>> str(Path(os.getcwd()).parents[0])
'/home'
>>> exit()
"""
"""
os.chdir(str(Path(os.getcwd()).parents[1]) + 'opt')
"""

"""
#!/usr/bin/env python3

from PIL import Image
import os
from pathlib import Path

for file in os.listdir():
  #print(file)
  if file == os.path.isfile(file):
    with Image.open(file) as im:
      print(im.format)
  else:
    continue

"""
