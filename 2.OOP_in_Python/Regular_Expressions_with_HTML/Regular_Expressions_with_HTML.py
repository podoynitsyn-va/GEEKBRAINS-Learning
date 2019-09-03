import requests
import re
from bs4 import BeautifulSoup as BS


#парсим html-код непосредственно с сайта
#или берём прямо из файла, если не получилось
try:
    geekbrains_text = requests.get("http://www.geekbrains.ru").text
except:
    with open('GeekBrains.htm','r',encoding="utf-8") as my_file:
        geekbrains_text = my_file.read()

# а). Через регулярные выражения
quantity = re.findall("<span class=\"total-users\">Нас уже ([0-9 ]+) человек</span>", geekbrains_text)[0]
count_users = int(quantity.replace(" ", ""))
print(f"Количество пользователей GeekBrains через регулярные выражения: {count_users}")

# b). Через библиотеку BeautifulSoup
soup = BS(geekbrains_text, 'html.parser')
sdf = soup.span.string
bs_count_users = int(''.join(x for x in sdf if x.isdigit()))
print(f"Количество пользователей GeekBrains через BeautifulSoup и генератор: {bs_count_users}")
