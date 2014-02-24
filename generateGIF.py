#!/usr/bin/env python

from images2gif import writeGif
from PIL import Image
import os
import datetime

yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")

file_names = sorted((fn for fn in os.listdir('./images/') if fn.endswith('.jpg') and fn.startswith(yesterday)))

images = [Image.open('./images/' + fn) for fn in file_names]

#size = (150,150)
#for im in images:
#    im.thumbnail(size, Image.ANTIALIAS)

filename = './gifs/' + yesterday + '.gif'
writeGif(filename, images, duration=0.2)
