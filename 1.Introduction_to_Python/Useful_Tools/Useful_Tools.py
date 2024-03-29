import math


def separator(sign):
    print()
    print(sign*33)


def task_name_separator(sign, task_number):
    print(sign*10+f' Задание № {task_number}'+sign*10)

#1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.


task_name_separator('-', 1)
list_1 = ['apple', 'orange', 'banana', 'plum', 'pineapple', 'lemon', 'apricot']
list_2 = ['apple', 'apricot', 'avocado', 'pineapple']
union_list = list(set(list_1) & set(list_2))
print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')
print(f'Список общих элементов первого и второго списков: {union_list}')
separator('*')
#2: Дан список, заполненный произвольными числами. Получить список из элементов исходного,
# удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.

task_name_separator('-', 2)
list_1 = [4, 6, -8, 34, 0, 56, -11, 50, 22, 91, 2, -33, -4, 25, 17, 44, 83, 12, 9, 27, 24]
list_2 = [number for number in list_1 if number % 3 == 0 and number > 0 and number % 4 != 0]

print(f'Исходный список: {list_1}')
print(f'Список, соответствующий условиям: {list_2}')
separator('*')
# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат
# (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]

task_name_separator('-', 3)
list_1 = [2, 1, 5, 9, -8, 0, 4, 16, -25, 25]
list_2 = [math.sqrt(number) if number > 0 else number for number in list_1]
print(f'Исходный список: {list_1}')
print(f'Модифицированный список: {list_2}')
separator('*')
# 4. Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError
# иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность возникновения исключительной ситуации,
# которая поднимается внутри функции.


def i_dont_want_number_13(number):
    if number == 13:
        raise ValueError
    else:
        return number**2


task_name_separator('-', 4)
user_number = int(input('Введите число от 1 до 100: '))
try:
    print(f'Квадрат вашего числа: {i_dont_want_number_13(user_number)}')
except:
    print('Я суеверный. Введите другое число!')
separator('*')
