import re

# 1. Получите текст из файла.
text = ''
with open('bbdf098ff5cb54f973d0c3b6d9b736e3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 2. Разбейте полученные текст на предложения.
sentences = re.split("[\.!?]\s", text)
print('\n', '-'*75, '\n')


# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
print('# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.\n')
pattern = re.compile('[а-яА-Я]{4,}')
words_list = pattern.findall(text)  # список стран, состоящий из 4+ букв.
words_list = [word.lower() for word in words_list]
words_dict = {}
for word in words_list:
    words_dict[word] = len(re.findall("\s" + word + "[!?\., ]", text.lower()))

words_list = list(words_dict.items())
list.sort(words_list, key=lambda param: param[1], reverse=True)
for index in range(10):
    print(f'word: {words_list[index][0]}, count: {words_list[index][1]}')
print('\n', '-'*75, '\n')

# 4. Отберите все ссылки.
print('# 4. Отберите все ссылки.\n')
pattern_str = '\w+\.?\w+\.\w+/?\w+'

pattern = re.compile(pattern_str)
links_list = pattern.findall(text)
print(links_list)
print('\n', '-'*75, '\n')

# 5. Ссылки на страницы какого домена встречаются чаще всего?
print('# 5. Ссылки на страницы какого домена встречаются чаще всего?\n')
pattern_str = '(\w+\.?\w+\.\w+)/?\w*'
pattern = re.compile(pattern_str)
domain_set = set(pattern.findall(str(links_list)))
domain_dict = {}
for domain in domain_set:
    domain_dict[domain] = len(re.findall(domain, text))
domain_dict = sorted(list(domain_dict.items()), key=lambda value: value[1], reverse=True)
print('Самый частый домен в тексте:', domain_dict[0][0])
print('\n', '-'*75, '\n')


# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
print('# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».\n')
link_pattern_str = '\w+\.?\w+\.\w+/?\w+'
new_text = re.sub(link_pattern_str, '«Ссылка отобразится после регистрации»', text)
print(new_text)
