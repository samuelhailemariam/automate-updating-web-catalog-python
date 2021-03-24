#!/usr/bin/env python3

import os
from PIL import Image

loc = '/mnt/c/Users/samue/Downloads/Coursera/Google IT Automation with Python/Course 6 - Automating Real-World Tasks/supplier-data/images'

def change_image(path):

    for image in os.listdir(path):
        try:
            img = Image.open(os.path.join(path, image))
            filename, ext = os.path.splitext(os.path.basename(os.path.join(path, image)))
            suffix = '.JPEG'
            img.resize((600,400)).convert('RGB').save(os.path.join(path, filename + suffix))
        except IOError:
            pass

if __name__ == "__main__":
    change_image(loc)