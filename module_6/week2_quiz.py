#!/usr/bin/env python3

import requests
import os

review_feedback_dict = {}
targetURL = ""


# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
for file in os.listdir():
    if os.path.isfile(file) and file.endswith("txt"):
        # You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
        with open(file) as feedback_f:
            info = feedback_f.readlines()
            title = info[0]
            name = info[1]
            date = info[2]
            feedback = info[3]
            # Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
            review_feedback_dict.update(
                [
                    ("title", title),
                    ("name", name),
                    ("date", date),
                    ("feedback", feedback),
                ]
            )
            print(review_feedback_dict)
            r = requests.post(targetURL, data=review_feedback_dict)
