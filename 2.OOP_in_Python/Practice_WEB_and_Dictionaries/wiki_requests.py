from requests import get
from bs4 import BeautifulSoup as BS
import re


def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link


def get_neighboring_links(topic):
    html_page = get_topic_page(topic)
    soup = BS(html_page, 'html.parser')

    # отбираем ссылки по паттерну '^\/wiki\/.*', чтобы исключить ссылки на других языках,
    # вроде таких 'https://sl.wikipedia.org/wiki/Drevo',
    # или служебные ссылки, вроде таких: 'https://meta.wikimedia.org/wiki/Privacy_policy/ru'
    # нам необходимы ссылки такого вида: '/wiki/%D0%A1%D0%B0%D0%B4'
    #начинающиеся с '/wiki/', при этом саму подстроку '/wiki/' исключим -
    # - она уже есть в корневой ссылке "https://ru.wikipedia.org/wiki/"

    links = ["https://ru.wikipedia.org/wiki/" + a.get('href')[6:] for a in soup.find_all(href=re.compile('^\/wiki\/.*'))]
    print(f'У страницы {topic} найдено {len(links)} соседних ссылок')
    return links


def get_topic_page(topic, multiple=False):
    link = get_link(topic)
    html_content = get(link).text
    return html_content


def get_n_page(link):
    html_content = get(link).text
    return html_content


def get_topic_words(topic, multiple=False):
    if multiple:
        print(f'Парсинг страницы {topic}')
        html_content = get_topic_page(topic, multiple)
        words = re.findall("[а-яёА-Я\-\']{3,}", html_content)
        print(f'Количество слов на странице {topic}: {len(words)}')
        print(f'Парсим соседние страницы...')
        count = 1
        for link in get_neighboring_links(topic):
            html_n_content = get_n_page(link)
            words_n = re.findall("[а-яёА-Я\-\']{3,}", html_n_content)
            print(f'Количество слов на странице {count}: {len(words_n)}')
            count +=1
            words = [*words, *words_n]

    else:
        print(f'Парсинг страницы {topic}')
        html_content = get_topic_page(topic, multiple)
        words = re.findall("[а-яёА-Я\-\']{3,}", html_content)
        print(f'Количество слов на странице {topic}: {len(words)}')
    return words



