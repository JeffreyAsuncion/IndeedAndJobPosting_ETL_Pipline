from datetime import datetime

class Job:

    def __init__(self, date_pulled, post, description, link):
        self.date_pulled = datetime.now()
        self.post = post
        self.description = description
        self.link = link
