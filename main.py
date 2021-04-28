from bs4 import BeautifulSoup
import lxml

with open('home.html', 'r') as html_file:   # r is read only
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')

    # find h5 tags
    # tags = soup.find('h5')       # finds first one
    # print(tag)

    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:

        print(course)
        # print(type(course))
