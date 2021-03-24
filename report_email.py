#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

path = '/mnt/c/Users/samue/Downloads/Coursera/Google IT Automation with Python/Course 6 - Automating Real-World Tasks/supplier-data/descriptions'



def process_text():
    summary = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            with open(os.path.join(path, file)) as f:
                result = f.readlines()
                report = {}
                report["name"] = result[0].strip()
                report["weight"] = int(result[1].strip().split()[0])
                summary.append(f'name: {report["name"]}')
                summary.append(f'weight: {report["weight"]} lbs')
                summary.append(f'\n')
    return summary
    
def main():
  """Process the JSON data and generate a full report out of it."""
  summary = process_text()
  # TODO: turn this into a PDF report
  paragraph = "<br/>".join(summary)
  title = "Processed Update on {}".format(date.today().strftime('%B %d, %Y'))
  attachment = f'{path}/processed.pdf'
  reports.generate_report(attachment, title, paragraph)

  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
    main()