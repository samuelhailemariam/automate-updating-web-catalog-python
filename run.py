#! /usr/bin/env python3

import os
import requests
import json


path = '/mnt/c/Users/samue/Downloads/Coursera/Google IT Automation with Python/Course 6 - Automating Real-World Tasks/supplier-data/descriptions'
url = 'http://[linux-instance-external-IP]/fruits'

for file in os.listdir(path):
    if file.endswith('.txt'):
        with open(os.path.join(path, file)) as f:
            result = f.readlines()
            product = {}
            product["name"] = result[0].strip()
            product["weight"] = int(result[1].strip().split()[0])
            product["description"] = result[2].strip()
            product["image_name"] = os.path.splitext(os.path.basename(os.path.join(path, file)))[0] + '.JPEG'
            product_json = json.dumps(product) 

            response = requests.post(url, json=product_json)
            
