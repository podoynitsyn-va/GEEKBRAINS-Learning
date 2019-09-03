import core
import re


topic = input('Введите слово: ')

words = core.get_topic_words(topic)
print(f'Выводить партянку из тысяч слов смысла нет, поэтому ограничимся количеством.')
print(f'Количество слов на странице {len(words)}')

with open('new.html', 'r', encoding='utf-8') as f:
    html = f.read()

links = core.get_link(html)

if len(links) > 10:
    cmd = input(f'Количество соседних ссылок {len(links)}. Парисинг потребует время. Оно Вам надо? Нажмите [y] что бы продолжить: ')
    if cmd != 'Y':
        exit()

for l in links:
    try:
        tmp = core.get_words_link(l)
    except:
        pass
    else:
        words += tmp

print(f'Количество слов на странице и соседних сслыках {len(words)}')
