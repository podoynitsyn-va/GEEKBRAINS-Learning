# Тема 4. Функции.
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

# Функционал проверки корректности ввода реализовывать не требовалось

def strNameAgeTown (name,age, town ) :
    srt_result = name[:1].upper()+name[1:] + ', ' + age + ' год(а), проживает в городе ' + town[:1].upper()+town[1:]
    return srt_result

name = input('Введите Ваше имя ')
age = input('Введите Ваш возраст ')
town = input('Введите город ВАшего проживания ')

print('Задание 4.1')
print()
print(strNameAgeTown (name, age, town))
print()


# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def maxNum (one,two, three) :
    list_num = [one,two, three]
    result = max(list_num)
    return result

print('Задание 4.2')
print()
print('Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них')
print()
print(maxNum(5,7,11), end= ' ')  # 11
print('- правильный ответ 11')
print(maxNum(9,6,2), end= ' ')   # 9
print('- правильный ответ 9')
print(maxNum(2,7,1), end= ' ')   # 7
print('- правильный ответ 7 ')
print()

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

print('Задание 4.3' )
print('')

name_pl = input('Введите имя Игрока ')
name_en = input('Введите имя Противника ')

persons = {'player' : [name_pl,100,25], 'enemy':[name_en,100,25]}   # Структура словаря {key : (NAME, health, damage), ...}
print(persons)
# Функция attack получает параметр damage атакующего и отнимает  это количество от health атакуемого.

def attack (person1,person2) :  # person1 - атакуемый
    global persons
    attacked_ = persons[person1]  # атакуемый
    attacking =  persons[person2]  # атакующий
    final_health =  attacked_[1] - attacking[2]
    persons[person1][1] = final_health
#_______________________________________________________________________________________________________

attack('player', 'enemy')
print(persons)

# Игра на выживание: damage  будем умножать на  случайное число от 0 до 1

import random

# Перепишем функцию attaack так чтобы сила удара была случайной
def attack (person1,person2) :  # person1 - атакуемый
    global persons
    attacked_ = persons[person1]  # атакуемый
    attacking =  persons[person2]  # атакующий
    rnd = random.random()
    final_health =  attacked_[1] - round(rnd*attacking[2])
    persons[person1][1] = final_health
    print(persons[person2][0], 'атаковал', persons[person1][0], ' с силой ', round(rnd*attacking[2]))
#_______________________________________________________________________________________________________

fl = False
iter = 0
while not fl :
    persons = {'player': [name_pl, 100, 25],
               'enemy': [name_en, 100, 25]}  # Структура словаря {key : (NAME, health, damage), ...}
    while not fl :
        iter = iter +1
        attack('player', 'enemy')
        attack('enemy', 'player')
        if (persons['player'][1] <= 0) and (persons['enemy'][1] > 0) :
            print ('Победил ', persons['enemy'][0]  )
            fl = True
        if (persons['player'][1] > 0) and (persons['enemy'][1] <= 0) :
            print ('Победил ', persons['player'][0]  )
            fl = True
        if (persons['player'][1] <= 0) and (persons['enemy'][1] <= 0) :
            print ('Ничья !!! ' )
            fl = True
        print(persons)
    print(' ')
    k = input("Нажимите  'y' для повтора игры...")
    print(' ')
    if k =='y':
        fl = False
    else:
        print('Досвидания! GTht[jlbv r pflfyb. 4.4.')
        fl = True

# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

persons = {'player' : [name_pl,100,25,1.2], 'enemy':[name_en,100,25,1.2]}   # Структура словаря {key : [NAME, health, damage, armor], ...}

print('Задание 4.4' )
print('')
print(persons)
print('')

#  Функцию damage -  вячисляет какой урон нанесет атакующий в зависимости от брони атакуемого
def damage (person1,person2) : # person1 - атакуемый
    global persons
    damage = persons[person2][2]/persons[person1][3]
    return damage
#_______________________________________________________________________________________________________

# Перепишем функцию attack
def attack4_4 (person1,person2) :  # person1 - атакуемый
    global persons
    attacked_ = persons[person1]  # атакуемый
    attacking =  persons[person2]  # атакующий
    rnd = random.random()
    strength = round(rnd*damage(person1, person2))
    final_health =  attacked_[1] - strength
    persons[person1][1] = final_health
    print(persons[person2][0], 'атаковал', persons[person1][0], ' с силой ', strength )
#_______________________________________________________________________________________________________

# Поиграем в выживание
fl = False
iter = 0
while not fl :
    persons = {'player' : [name_pl,100,25,1.2], 'enemy':[name_en,100,25,1.2]}   # Структура словаря {key : [NAME, health, damage, armor], ...}
    iter = 0
    print('Состояние персон на старте',persons)
    while not fl :
        iter = iter +1
        attack4_4('player', 'enemy')
        attack4_4('enemy', 'player')
        if (persons['player'][1] <= 0) and (persons['enemy'][1] > 0) :
            print('')
            print ('Победил ', persons['enemy'][0], ' на ', iter, ' ходу'  )
            fl = True
        if (persons['player'][1] > 0) and (persons['enemy'][1] <= 0) :
            print('')
            print ('Победил ', persons['player'][0], ' на ', iter, ' ходу'  )
            fl = True
        if (persons['player'][1] <= 0) and (persons['enemy'][1] <= 0) :
            print('')
            print ('Ничья !!!  на ', iter, ' ходу'   )
            fl = True
    print('Состояние персон в конце', persons)
    print('')
    k = input("Нажимите  'y' для повтора игры...")
    print(' ')
    if k =='y':
        fl = False
    else:
        print('Досвидания!')
        fl = True