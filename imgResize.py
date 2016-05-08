#!/usr/bin/env python
# - open all images in the directory /glob/
# - convert to greyscale
# - sharpen with unsharp mask
# - resize width: 1024
# - save all resized_ pre
# - lpr print all resized_

import subprocess, glob, time
from PIL import Image, ImageFilter

basewidth = 1024
for filename in glob.glob('*.[jJ][pP]*[gG]'):
    img = Image.open(filename).convert('L').filter(ImageFilter.UnsharpMask(
        radius=10, percent=200, threshold=3))
    
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    
    img.save('resized_' + filename)
    time.sleep(1)
    subprocess.Popen(['lpr', 'resized_' + filename])
    time.sleep(6)

# set to default printer:
# sudo lpoptions -d Xerox_Phaser_3140
