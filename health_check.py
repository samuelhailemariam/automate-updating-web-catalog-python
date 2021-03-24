#!/usr/bin/env python3

import psutil
import emails
import os
import subprocess as sp

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
if cpu_usage > 80.0:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
    
disk_percent_usage = psutil.disk_usage('/')[-1]
if disk_percent_usage < 20.0:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)
    
mem_usage = psutil.virtual_memory()
THRESHOLD = 500 * 1024 * 1024
if mem_usage.available < THRESHOLD:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

if not sp.run(['ping', '-c 2', 'localhost']).check_returncode():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)



