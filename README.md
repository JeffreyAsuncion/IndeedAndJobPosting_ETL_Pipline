# WebScraping_BeautifulSoup
Web Scraping with Python and Beautiful Soup


to set up pipenv virtual environment
------------------------------------
please install the following

> pipenv install beautifulsoup4
install a parser
> pipenv install lxml
to make web request
> pipenv install requests



Purpose : Create an ETL that will scrape a website for Jobs Posting and store in a SQLite3 Database 

JobPost000.py : demo pulling data from a static website
JobPost001.py : jobs on a job site & get additional info for each job (skills, info)
JobPost002.py : get the most recent job posts
JobPost003.py : filter out an unfamilar skill
JobPost004.py : automatic on a timer
JobPost005.py : write results to a file
JobPost006.py : write to Database
JobPost007.py : Job Class
JobPost008.py : add Date_pulled to Class and refactor code to include the date_scraped
