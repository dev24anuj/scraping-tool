from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    # print("HTML content---->",content)
#by line 6 and 7 you can scrap whole html file 
soup = BeautifulSoup(content,'lxml')
# print(soup.prettify())

#from line 11 and 12 you can scrap specafic things 
# course_html_tags = soup.find_all('a')
# print(tags)
# for course in course_html_tags:
#     print("Falna",course)
course_card =soup.find_all('div', class_='card')
for course in course_card:
    print(course.h5)