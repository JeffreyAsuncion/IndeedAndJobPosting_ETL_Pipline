from datetime import datetime

class Job:

    def __init__(self, date_pulled, post, description, link):
        self.date_pulled = date_pulled
        self.post = post
        self.description = description
        self.link = link
