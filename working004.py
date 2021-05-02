import requests
from bs4 import BeautifulSoup
import pandas as pd

def format_str(input_str):
    if len(input_str) == 1:
        return input_str
    else:
        word_list = input_str.split()
        word_str = word_list.pop(0) #init str with first word
        for word in word_list:
            word_str = f"{word_str}+{word}"
        return word_str

# the 'job_name' and 'city', 'state' can be passed to the url query
def extract(page, job_name="Python Developer", city_name="New York", state_abbr="NY"):
    """
        page (int)
        job_name (str)
        city (str) full name
        state (str) 2 Letter Abrreviation
    """
    # input check needs to be implemented
    job_str = format_str(job_name)
    city_str = format_str(city_name)
    state_str = state_abbr

    #google 'my user agent'
    my_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    headers = {'User-Agent' : my_user_agent}
    # url = f'https://www.indeed.com/jobs?q=python+developer&l=New+York%2C+NY&start={page}'
    url = f'https://www.indeed.com/jobs?q={job_str}&l={city_str}%2C+{state_abbr}&start={page}'

    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    return soup

# known errors
# . if job_name doesnot return results in indeed Empty data frame is produced


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




joblist = []

for i in range(0, 50, 10): # This loops thru 200/10 pages 20 pages
    print(f"Getting page, {i}")
    # job_name = "Fudrucker"
    c = extract(i) # will give an error if result has less than 4 pages 
    transform(c)
    # print(len(joblist))
    # print(joblist)

df = pd.DataFrame(joblist)
print(df.head(10))
print(df.tail(10))

df.to_csv('jobs.csv')

