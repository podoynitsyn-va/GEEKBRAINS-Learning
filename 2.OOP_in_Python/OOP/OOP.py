# Это задание продолжает практическое задание прошлого урока. За основу возьмите свой код с классами Word и Sentence.
# Выполним с ним следующие преобразования:
# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
# Подсказка: теперь в нём не нужно хранить части речи.
# words = []
# words.append(Noun("собака"))
# words.append(Verb("ела"))
# words.append(Noun("колбасу"))
# words.append(Noun("кот"))
# По желанию добавьте ещё несколько глаголов и существительных.
# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
# Подсказка: ранее part был свойством класса Word, а теперь это метод классов Noun и Verb.


class Word:
    def __init__(self, text):
        self.text = text


class Sentence:
    def __init__(self, content, my_list):
        self.content = content
        self.my_list = my_list

    def show(self):
        my_sentence = []
        words_list = create_words(self.my_list)
        for count in self.content:
            my_sentence.append(words_list[count].text)
        print(" ".join(my_sentence))

    def show_parts(self):
        my_parts = []
        words_list = create_words(self.my_list)
        for count in self.content:
            my_parts.append(words_list[count].part())
        print(" ".join(set(my_parts)))


class Noun(Word):
    __grammar = "сущ"

    def part(self):
        return "существительное"


class Verb(Word):
    __grammar = "гл"

    def part(self):
        return "глагол"


class Adverb(Word):
    __grammar = "нар"

    def part(self):
        return "наречие"

    
class Pretext(Word):
    __grammar = "пред"

    def part(self):
        return "предлог"


def create_words(my_list):
    words_list = []
    for element in my_list:
        words_list.append(get_words(element))
    return words_list


def get_words(word_element):
    if word_element[1] == "сущ":
        return Noun(word_element[0])
    elif word_element[1] == "глагол":
        return Verb(word_element[0])
    elif word_element[1] == "наречие":
        return Adverb(word_element[0])
    elif word_element[1] == "предлог":
        return Pretext(word_element[0])
    else:
        return None


words = [["собака", "сущ"],
        ["ела", "глагол"],
        ["колбасу", "сущ"],
        ["вечером", "наречие"],
        ["из", "предлог"],
        ["холодильника", "сущ"]]

content = [0, 1, 3, 4, 5]

my_sentence = Sentence(content, words)
my_sentence.show()
my_sentence.show_parts()


