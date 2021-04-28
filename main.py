from bs4 import BeautifulSoup
import lxml

with open('home.html', 'r') as html_file:   # r is read only
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')

    # find h5 tags
    # tags = soup.find('h5')       # finds first one
    # print(tag)
    ##########################################

    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:

    #     print(course.text)
    #     print(type(course.text))
 
    ###########################

    course_cards = soup.find_all('div', class_='card')
    # print(course_cards)
    for course in course_cards:
        course_name = course.h5
        course_price = course.a

        print(course_name.text)
        print(course_price.text)
        print()