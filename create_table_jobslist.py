# run once to create table

# CREATE table
import sqlite3

conn = sqlite3.connect('jobslist.db')

cursor = conn.cursor()
sql="""CREATE TABLE jobslist (
        date_pulled DATE,
        job_post TEXT,
        description TEXT,
        link TEXT
)"""
cursor.execute(sql)

cursor.commit()
cursor.close()
