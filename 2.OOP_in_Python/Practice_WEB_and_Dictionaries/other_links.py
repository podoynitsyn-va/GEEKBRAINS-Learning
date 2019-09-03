from requests import get
from bs4 import BeautifulSoup as BS
import re


def get_topic_page(topic):
    link = get_link(topic)
    #html_content = get(link).text
    html_content = get(link).text
    return html_content


def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    print(type(link))
    return link


topic = 'Дерево' #input("Введите ключевое слово поиска: ")
html_page = get_topic_page(topic)
soup = BS(html_page, 'html.parser')

# отбираем ссылки по паттерну '^\/wiki\/.*', чтобы исключить ссылки на других языках,
# вроде таких 'https://sl.wikipedia.org/wiki/Drevo',
# или служебные ссылки, вроде таких: 'https://meta.wikimedia.org/wiki/Privacy_policy/ru'
# нам необходимы ссылки такого вида: '/wiki/%D0%A1%D0%B0%D0%B4'
#начинающиеся с '/wiki/', при этом саму подстроку '/wiki/' исключим -
# - она уже есть в корневой ссылке "https://ru.wikipedia.org/wiki/"

links = ["https://ru.wikipedia.org/wiki/" + a.get('href')[6:] for a in soup.find_all(href=re.compile('^\/wiki\/.*'))]
print(type(links))
for link in links:
    print(link)
