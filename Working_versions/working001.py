import requests
from bs4 import BeautifulSoup

def extract(page):
    #google 'my user agent'
    my_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    headers = {'User-Agent' : my_user_agent}
    url = f'https://www.indeed.com/jobs?q=python+developer&l=New+York%2C+NY&start={page}'

    r = requests.get(url, headers)
    return r.status_code

print(extract(0))


