from Task5 import Word, Sentence

# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
class Noun(Word):
    __grammar = "сущ"
    def __init__(self, text):
        self.text = text
        self.__part = "существительное"
    @property
    def part(self):
        return self.__part

class Verb(Word):
    __grammar = "гл"
    def __init__(self, text):
        self.text = text
        self.__part = "глагол"
    @property
    def part(self):
        return self.__part

# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.

words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))

print("Проверка 4-ого задания:")
print(type(words))
print(type(words[0]))
print(type(words[1]))
print(words[1].part)

# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
print("\nПроверка 5-ого задания:")
sample = Sentence(words, [0,1,2])
print(sample.show())


# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
print("\nПроверка 6-ого задания:")
print(words[0].part)


# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
print("\nПроверка 7-ого задания:")
print(sample.show_parts())