# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

numbers = [3, 882, 8]


def max_value(*args):
    return max(*args)


print(max_value(numbers))
