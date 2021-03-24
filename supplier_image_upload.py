#!/usr/bin/env python3

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module
loc = "/mnt/c/Users/samue/Downloads/Coursera/Google IT Automation with Python/Course 6 - Automating Real-World Tasks/supplier-data/images"
url = "http://localhost/upload/"

for image in os.listdir(loc):
    if image.endswith('.JPEG'):
        try:
            with open(os.path.join(loc, image), 'rb') as opened:
                r = requests.post(url, files={'file': opened})
        except IOError:
            pass



