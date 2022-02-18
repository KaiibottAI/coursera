#!/usr/bin/env python3

import requests
import os

review = {}
targetURL = "http://104.197.46.253"
feedbackURL = "http://104.197.46.253/feedback/"
path = "/data/feedback/"

for file in os.listdir(path):
    if os.path.isfile(path + file):
        with open(path + file) as feedback_f:
            info = feedback_f.readlines()
            title = info[0]
            name = info[1]
            date = info[2]
            feedback = info[3]
            review.update(
                [
                    ("title", title.strip()),
                    ("name", name.strip()),
                    ("date", date.strip()),
                    ("feedback", feedback.strip()),
                ]
            )

            r = requests.post(feedbackURL, data=review)
            print(r.status_code)
