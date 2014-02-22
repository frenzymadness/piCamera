#!/usr/bin/env python

import picamera
import time

now = time.strftime('%Y-%m-%d_%H:%M:%S')

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.capture('./images/' + now + '.jpg')

