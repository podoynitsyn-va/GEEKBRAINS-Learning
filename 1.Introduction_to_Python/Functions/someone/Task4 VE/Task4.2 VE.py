#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def function2(a, b, c):
    return max(a, b, c)

i = 0
numbers = []
while i < 3:
    numbers.append(int(input("Введите число: ")))
    i += 1

answer = function2(numbers[0], numbers[1], numbers[2])
print(answer)