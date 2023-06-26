import requests
from bs4 import BeautifulSoup

def extract(page):
    #google 'my user agent'
    my_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    headers = {'User-Agent' : my_user_agent}
    url = f'https://www.indeed.com/jobs?q=python+developer&l=New+York%2C+NY&start={page}'

    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        # not every post has salary
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = 'Not Available'
        summary = item.find('div', {'class' : 'summary'}).text.strip().replace('\n', '')

        job = {
            'title' : title,
            'company' : company,
            'salary' : salary,
            'summary' : summary
        }

        joblist.append(job)
    
    return

# 16:30


joblist = []
c = extract(0)
transform(c)
print(len(joblist))
print(joblist)


