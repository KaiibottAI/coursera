```bash
ls ~/
```

```bash
sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
```

```bash
tar xf ~/supplier-data.tar.gz
```

```bash
ls ~/supplier-data
```

```bash
cat ~/supplier-data/descriptions/007.txt
```

./changeImage.py
```python
#!/usr/bin/env python3

from PIL import Image
import os

src = "~/supplier-data/images/"

for file in os.path(src):
    if os.path.isfile(src + file):
        try:
            with Image.open(src+file) as im:
                im = im.convert("RGB")
                im.resize((600, 400))
                im.save(src + file + ".jpg")
        except:
            print(f"{file} not an image")
```

./supplier_image_upload.py
```python
#!/usr/bin/env python3

import requests
import os

src = "~/supplier-data/images/"

url = ""
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

for pic in os.listdir(src):
    r = requests.post(url, files={src+pic : opened})

```


./run.py
```python
#!/usr/bin/env python3

import os
import requests


```