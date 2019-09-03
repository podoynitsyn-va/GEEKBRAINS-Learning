import re
from wiki_requests import get_topic_page


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яёА-Я\-\']{3,}", html_content)
    #text = " ".join(words)
    return words


def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(topic, num_start, num_finish):
    words = get_common_words(topic)
    for w in words[num_start:num_finish]:
        print(w)


def main():
    topic = input("Введите ключевое слово поиска: ")
    num_start = int(input("начальный номер вывода из списка: "))
    num_finish = int(input("конечный номер вывода из списка: "))
    visualize_common_words(topic, num_start, num_finish)

main()
