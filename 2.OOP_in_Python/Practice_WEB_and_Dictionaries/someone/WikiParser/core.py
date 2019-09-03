import requests
import re
from bs4 import BeautifulSoup as BS
from collections import Counter


def get_link_wiki():
    return 'https://ru.wikipedia.org'


def print_list(lst):
    for l in lst: print(l)


def get_content_link(link):
    html = requests.get(link).text
    with open('new.html', 'w', encoding='utf-8') as f:
        f.write(html)
    return html


def get_topic(topic):
    return get_link_wiki() + '/wiki/' + topic.capitalize()


def get_topic_page(topic):
    link = get_topic(topic)
    return get_content_link(link)


def get_link(html):
    soup = BS(html, "html.parser")
    links = [l["href"] for l in soup.find_all('a') if l.get("href", None)]
    links = " ".join(links)
    links = re.findall('/wiki/[^\s"]+', links)
    links = list(filter(lambda l: l.find('.jpg')+l.find('.svg') == -2, links))
    links = set(map(lambda l: get_link_wiki() + l, links))
    return links


def get_words_html(html_content):
    return re.findall("[а-яА-я\-\']{3,}",html_content)


def get_words_link(link):
    return get_words_html(get_content_link(link))


def get_topic_words(topic):
    return get_words_html(get_topic_page(topic))


def get_rate_words(words_list):
    rate_list = list(Counter(words_list).items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def get_common_words(topic):
    return get_rate_words(get_topic_words(topic))



if __name__ == '__main__':
    html = get_topic_page('Орск')
    print_list(get_link(html))
