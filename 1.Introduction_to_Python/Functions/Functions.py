# Тема 4. Функции.
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида
# «Василий, 21 год(а), проживает в городе Москва»
# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# #### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# # ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона
# и вычитания его из здоровья персонажа.

def separator(sign):
    print()
    print(sign*33)

def task_name_separator(sign, task_number):
    print(sign*10+f' Задание № {task_number}'+sign*10)

#Задание 1
def user_info(name, age, city):
    print(f'{name}, {age} лет, проживает в городе {city}')

separator('*')
task_name_separator('-',1)
name = input('Введите имя: ');
age = input('Введите возраст: ')
city = input('Введите город проживания: ')
user_info(name,age,city)

#Задание 2
def max_number(number1,number2,number3):
    return max(number1,number2,number3)

def max_two(number1,number2):
    if number1 <= number2:
        return number2
    return number1
def max_three(number1,number2,number3):
    return max_two(number1,max_two(number2,number3))

separator('*')
task_name_separator('-',2)
my_list = []
number1 = int(input('Введите число № 1: '))
number2 = int(input('Введите число № 2: '))
number3 = int(input('Введите число № 3: '))
#через объявленную функцию
print(max_number(number1,number2,number3))
#через лямбда-функцию
max_num = lambda x,y,z:max(x,y,z)
print(max_num(number1,number2,number3))
#без функции max
print(max_three(number1,number2,number3))

#Задание 3
def input_player(num):
    name = input(f'Введите имя игрока {num}: ')
    health = int(input(f'Введите уровень здоровья игрока {num}: '))
    damage = int(input(f'Введите уровень урона игрока {num}: '))
    return {'name':name,'health':health,'damage':damage,'armor':1}

def input_armor(person):
    armor = float(input(f'Введите уровень надежности бронежилета {person["name"]} (от 1 до 2, например 1.3): '))
    person['armor'] = armor

def get_damage(person1,person2):
    old_health = person2['health']
    person2['health'] = person2['health'] - person1['damage'] / person2['armor']
    separator('-')
    print(f'Уровень здоровья у {person2["name"]} теперь становится равен {old_health}-{person1["damage"] }/{person2["armor"]} = { round(person2["health"],2)}')
    separator('-')

def attack(person1,person2):
    separator('=')
    print(f'{person1["name"]} внезапно осуществляет атаку на {person2["name"]}')
    get_damage(person1,person2)
    if person2['health']<=0:
        print(f'Атака {person1["name"]} была слишком сильна, {person2["name"]} покинул этот мир...')
    else:
        print(f'''{person2["name"]} зашатался, но устоял и сейчас даст сдачи
              Удар!''')
        get_damage(person2, person1)
        if person1['health'] <= 0:
            print(f'Атака {person2["name"]} удалась, {person1["name"]} получил по заслугам...')
        else:
            print(f'Атака {person2["name"]} была сильна, но {person1["name"]} удержался...')
            print(f'{person1["name"]} и {person2["name"]} одумались, помирились и пошли в ближайший бар раздавить по пивку...')

separator('*')
task_name_separator('-',3)

player1 = input_player(1)
player2 = input_player(2)
attack(player1,player2)

#если оба противника остались живы, то битва продолжается
#Задание 4
if player1['health']>0 and player2['health']>0:
    separator('*')
    task_name_separator('-', 4)
    print(f'В баре {player1["name"]} и {player2["name"]} не поделили красивую девчонку и вышли на улицу "поговорить"')
    print('Но в этот раз они схитрили, и втайне друг от друга надели бронежилеты,'
          'которые спёрли у охранников в баре')
    input_armor(player1)
    input_armor(player2)
    attack(player1,player2)


