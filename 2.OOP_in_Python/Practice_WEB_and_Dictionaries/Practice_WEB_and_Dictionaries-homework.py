# Упражнение продолжает практическую работу из последнего видеоурока.
# Для усовершенствования приложения разберитесь, как можно реализовать получение common words с соседних страниц
# — тех, на которые есть ссылки.
# Возможен следующий алгоритм решения задачи:
# 1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup.
# Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии.
# (Вы можете распознать их по тексту \wiki).
# 2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
# 3. Сложить все в один список.

from wiki_requests import get_topic_page, get_topic_words


def get_common_words(topic, multiple):
    words_list = get_topic_words(topic, multiple)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(topic, num_start, num_finish, multiple):
    words = get_common_words(topic, multiple)
    if multiple:
        print(f"Слова, находящиеся на позициях с {num_start} по {num_finish} на странице Википедии {topic} и соседних страницах:")
    else:
        print(f"Слова, находящиеся на позициях с {num_start} по {num_finish} на странице Википедии {topic}:")
    for w in words[num_start:num_finish]:
        print(w)


def main():
    topic = input("Введите ключевое слово поиска: ")
    num_start = int(input("начальный номер вывода из списка: "))
    num_finish = int(input("конечный номер вывода из списка: "))
    visualize_common_words(topic, num_start, num_finish, False)
    visualize_common_words(topic, num_start, num_finish, True)

main()
