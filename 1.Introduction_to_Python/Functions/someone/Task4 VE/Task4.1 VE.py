#1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека

def function1 (name, age, city):
    return("{}, {} год(а), проживает в городе {}".format(name, age, city))

name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город проживания: ")
answer = function1(name, age, city)
print(answer)