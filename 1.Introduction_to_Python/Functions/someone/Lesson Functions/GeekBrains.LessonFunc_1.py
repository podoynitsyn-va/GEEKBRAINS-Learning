#1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

name = input('Введите имя: ')
age = int(input('Введите возраст: '))
city = input('Введите город: ')
age_list = [4, 5, 6, 7, 8, 9, 0]
age_cut = age % 10

if (int(age) > 10 and int(age) < 14) or age_cut in age_list:
	suffix = 'лет'
else:
	suffix = 'год(а)'

def user_info(name, age, city):
    return f'{name}, {age} {suffix}, проживает в городе {city}'

print(user_info(name, age, city))
