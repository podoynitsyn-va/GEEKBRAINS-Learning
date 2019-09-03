import re
from  bs4 import BeautifulSoup as BS
import requests

def get_link (topic):
   html_link ='https://ru.wikipedia.org/wiki/'+topic.capitalize()
   return html_link

def get_topic_page(topic) :
    link = get_link(topic)
    #print(link)
    response = requests.get(link)
    page = ''
    if response.status_code == 200:
        page = requests.get(link).text
    else:
        print(f'Ссылка  {link} не верна или не возможно установить соединение с сайтом')
    return page

def get_topic_words(topic) :
    content = get_topic_page(topic)
    words = re.findall("[-а-яА-Я\n']{3,}",content)
    return words

def get_common_words(words_list):
    rate = {}
    for word in words_list :
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key = lambda  x: -x[1])
    return rate_list

def vis_com_words(word_list) :
    list_num = []
    print('\n','Введите число, максимально,  сколько раз встречающиеся слова необходимо вывести?')
    for word, num in word_list:
        list_num.append(num)
    print(f'Всего слов в списке {len(word_list)} максимальное количество = {max(list_num)}, минимальное {min(list_num)}')
    start= int(input(f'Введите целое число >= 0, проверка не выполняется):' ))
    #print(list_num)
    temp_list = list_num.copy()
    temp_list.reverse()
    #print(temp_list)
    temp = 0
    for temp1 in temp_list :
        if temp1 >= start :
            temp = temp1
            break
        else:
            temp = len(temp_list)
    #print('temp', temp)
    ind_temp = temp_list.index(temp,0,len(temp_list))
    #print(ind_temp)
    indx =  len(temp_list)-ind_temp-1
    #print('indx', indx)
    #print(word_list[0:1])
    l = word_list[0:indx+1]
    #print(len(l))
    for w, n in l:
        print(f'Слово {w}, встречается {n}  раз')




#https://ru.wikipedia.org/wiki/Дерево


#Упражнение продолжает практическую работу из последнего видеоурока. Для усовершенствования приложения разберитесь, как
# можно реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
#Возможен следующий алгоритм решения задачи:
#1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup.
#Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии.
#(Вы можете распознать их по тексту \wiki).
#2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
#3. Сложить все в один список

print('\n', '-' * 30, 'Задание  №1-3', '-' * 30, '\n')


topic = input('Введите тему  Wiki на русском языке:')
link = get_link((topic))
print('Поиск в Wiki по ссылке ', link)
page = get_topic_page(topic)
words_list = get_topic_words((topic))  # список слов с интересуемой страницы

soup = BS(page, 'html.parser')
all_a = soup.find_all('a') #, attrs='href')
all_wiki_page = []  # Пустой список соседних страниц. Соседней считаем страницу имеющую в записи адреса ссылки подстроку вида "/wiki/"
str_neighbour = r"/wiki/"
find_str = re.compile(r"/wiki/")
count = 1  # Счетчик остановки загрузки страниц, установлен в 100
count2 = 1  # Счетчик кол-ва соседей
for n in all_a :
    search_res = re.search(find_str, n.get('href', ""))
    print(f' {count2}). Результат изучения атрибута тэга  {n}  :','\n',  search_res)
    count2  +=1
    if  search_res != None:
        all_wiki_page.append((n.get('href', "")))
        count += 1  #  Плюс одна страница в списке на загрузку
        topic_list = re.findall(r"/wiki/(.{1,})", n.get('href', ""))   # зачищаем ссылку (тип - list) перед загрузкой
        topic = ''.join(topic_list)   # Формируем ссылку
        words_list_neighbour = get_topic_words((topic))  # Загружаем слова с соседней страницы
        words_list = words_list + words_list_neighbour  # Добавляем загруженные слова с соседней страницы в список слов стартовой страницы
        if count == 25 : break   # пора спать....

common_words = get_common_words(words_list)   # Наведем лоск
vis_com_words(common_words)                      # Итоги !!!


