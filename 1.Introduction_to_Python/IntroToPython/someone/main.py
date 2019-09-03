# #1
# print('Задание №1')
# number = int(input('Введите число'))
# print(number + 2)
# #2
# print('Задание №2')
# number = int(input('Введите число'))
# while number <= 0 or number >= 10:
#     print('Вы ввели неверное число, число должно быть больше 0, но меньше 10')
#     number = int(input('Введите число'))
# number = number ** 2
# print('Квадрат введеного числа равен ' + str(number))
#3
print('Задание №3')
print('Медицинская анкета')
name = input('Как Ваше имя?')
soname = input('Какая Ваша фамилия?')
age = int(input('Сколько Вам лет?'))
weight = int(input('Сколько Вы весите?'))
print('Результаты анкетирования:')
result = ''
if age < 30 and weight > 50 and weight < 120:
    result = 'хорошее состояние'
elif age > 30 and age < 40 and (weight < 50 or weight > 120):
    result = 'следует заняться собой'
elif age > 40 and (weight < 50 or weight > 120):
    result = 'следует обратиться к врачу!'
print(name + ' ' + soname + ', ' + str(age) + ' год, вес ' + str(weight) + ' - ' + result)
