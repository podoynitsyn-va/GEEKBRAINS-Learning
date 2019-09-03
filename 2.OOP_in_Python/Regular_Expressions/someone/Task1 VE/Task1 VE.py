#1. Получите текст из файла.
print("РЕШЕНИЕ ПЕРВОЙ ЗАДАЧИ: ")
f = open("bbdf098ff5cb54f973d0c3b6d9b736e3.txt", "r", encoding="utf-8")
data = f.read()
print(data)


#2. Разбейте полученные текст на предложения.
import re

print("\nРЕШЕНИЕ ВТОРОЙ ЗАДАЧИ: ")
sentence = re.split("[?!\.][^mailru/]", data)
for line in sentence:
    print(line)


#3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
print("\nРЕШЕНИЕ ТРЕТЬЕЙ ЗАДАЧИ: ")

words = re.findall("[a-zA-Zа-яА-Я]{4}\w*", data)

def top(list, n):
    frequency = {}
    for w in list:
        w = w.lower()
        count = frequency.get(w, 0)
        frequency[w] = count + 1
    i = 0
    top = []
    list = sorted(frequency.items(), key=lambda value: value[1], reverse=True)
    while i < n:
        top.append(list[i])
        i += 1
    return top

print(top(words, 10))


# 4. Отберите все ссылки.
print("\nРЕШЕНИЕ ЧЕТВЕРТОЙ ЗАДАЧИ: ")
pattern = re.compile("\w*\.?\w*\.ru/?\w*")
print(pattern.findall(data))


# 5. Ссылки на страницы какого домена встречаются чаще всего?
print("\nРЕШЕНИЕ ПЯТОЙ ЗАДАЧИ: ")
pattern = re.compile("\w*\.?\w*\.ru")
link = pattern.findall(data)
print(top(link, 1))


# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации»
print("\nРЕШЕНИЕ ШЕСТОЙ ЗАДАЧИ: ")
text = re.sub("\w*\.?\w*\.ru/?\w*", "«Ссылка отобразится после регистрации»", data)
print(text)

