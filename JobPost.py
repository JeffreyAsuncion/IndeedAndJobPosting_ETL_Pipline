# add timestamp

from bs4 import BeautifulSoup
import requests
import time
import sqlite3
from Jobs import Job
from datetime import datetime

# Next steps try with multiple unfamiliar skills
print("Put some skill that you are not familiar with.") 
unfamiliar_skill = input("> ") 
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    # Connect to database
    conn = sqlite3.connect('jobslist.db')
    # Create cursor
    cursor = conn.cursor()


    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):

        published_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date:
            # clean up scraped data            
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')      #replace is to clean the whitespaces
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            
            # add class
            date_pulled = datetime.now()
            post = company_name.strip()
            description = skills.strip()
            link = more_info
            J = Job(date_pulled, post, description, link)


            if unfamiliar_skill not in skills:
                print(f"Date pulled: {J.date_pulled}")
                print(f"Company Name: {J.post}") 
                print(f"Required Skills: {J.description}")
                print(f"More Info: {J.link}")
                print("~" * 20)
                cursor.execute("INSERT INTO jobslist VALUES(?, ?, ?, ?)" , (J.date_pulled, J.post, J.description, J.link))
                conn.commit()
    
    conn.close()

    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)