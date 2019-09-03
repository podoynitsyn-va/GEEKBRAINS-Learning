import re
from collections import Counter


def separator(sign):
    print()
    print(sign*33)


def task_name_separator(sign, task_number):
    print(sign*10+f' Задание № {task_number}'+sign*10)

# 1. Получите текст из файла.
# Примечание: Можете взять свой текст или воспользоваться готовым из материалов к уроку.
# Вспомните операции с чтением файлов и не забудьте сохранить текст в переменную по аналогии с видеоуроками.


task_name_separator('-', 1)

with open('homework_data.txt', 'r') as my_file:
    my_text = my_file.read()
    my_file.close()
print("Исходный текст:")
print(my_text)
separator('*')

# 2. Разбейте полученный текст на предложения.
# Примечание: Напоминаем, что в русском языке предложения заканчиваются на ., ! или ?.


def sentence_division(your_text):
    pattern_sentence = "[\.\?\!]\s"
    sentences = re.split(pattern_sentence, your_text)
    for sentence in sentences:
        print(sentence)


task_name_separator('-', 2)
print("Деление текста на предложения:")
sentence_division(my_text)
separator('*')
# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
# Пример вывода: [(“привет”, 3), (“люди”, 3), (“город”, 2)].


def counter_words(words_text, number):
    counter_dict = Counter(words_text)
    print(f"Первые {number} слов через Counter:")
    for key in sorted(counter_dict, key=counter_dict.get, reverse=True)[:number]:
        print(key, counter_dict[key])


def enumeration_words(words_text, number):
    enumeration_dict = {}
    for word in words:
        enumeration_dict[word] = enumeration_dict.get(word, 0)+1
    count = 0
    print(f"Первые {number} слов через формирование пар словаря:")
    for key in sorted(enumeration_dict, key=enumeration_dict.get, reverse=True)[:number]:
        print(key, enumeration_dict[key])


task_name_separator('-', 3)
pattern_word = r'\w{4,}'
words = re.findall(pattern_word, my_text)
for i in range(0, len(words)):
    words[i] = words[i].lower()
print("Список слов, содержащих более 4 букв:")
print(words)

#1 способ - через collections.Counter
counter_words(words, 10)
separator('-')
#2 способ - перебором элементов списка
enumeration_words(words, 10)
separator('*')

# 4. Отберите все ссылки.
# Примечание: Для поиска воспользуйтесь методом compile, в который вы вставите свой шаблон для поиска ссылок в тексте.


def get_pattern_links():
    return "\S+\.ru\/?\w*"


def get_links(your_text):
    pattern_links = re.compile(get_pattern_links())
    print("Список ссылок из текста:")
    return pattern_links.findall(your_text)


task_name_separator('-', 4)
print(get_links(my_text.lower()))
separator('*')

# 5. Ссылки на страницы какого домена встречаются чаще всего?
# Напоминаем, что доменное имя — часть ссылки до первого символа «слеш».
# Например в ссылке вида travel.mail.ru/travel?id=5 доменным именем является travel.mail.ru.
# Подсчет частоты сделайте по аналогии с заданием 3, но верните только одну самую частую ссылку.

task_name_separator('-', 5)

pattern_dom = "\S+\.ru"
dom_list = re.findall(pattern_dom, my_text.lower())
print("Наиболее часто встречающееся доменное имя:")
counter_words(dom_list, 1)
separator('*')

# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
task_name_separator('-', 6)
print("Заменяем ссылки на необходимый текст:")

print(re.sub(get_pattern_links(), '"Ссылка отобразится после регистрации"', my_text))
separator('*')
