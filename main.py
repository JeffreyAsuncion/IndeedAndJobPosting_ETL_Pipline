from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:   # r is read only
    content = html_file.read()
    print(content)