# # Упражнение  1
#
# print('Упражнение 1','\n')
# number = int(input('Введите число: '))
# print('Ответ:', number + 2)
#
# # Упражнение  2
#
# print('\n','Упражнение 2','\n',sep='')
# number = 0
# while number <= 0 or number >= 10:
#     number = int(input('Введите число: '))
#     if number <= 0 or number >= 10:
#         print('Число неверное, диапозон допустимых чисел (0, 10)', 'Попробуйте снова!', sep='\n')
# print('Ответ:', number ** 2)
#
# # Упражнение  3
# # Медицинская анкета

print('\n','Упражнение 3','\n',sep='')
#Ввод параметров
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))
print(name, surname, end=', ')
print(age, 'год', end=', ')
print('вес', weight, end=' - ')

#Хорошее состояние
if age <= 30 and 50 <= weight <= 120:
    print('у вас все хорошо, так держать!')
#Следует заняться собой / следует обратиться к врачу
elif age > 30 and weight < 50 or weight > 120:
    if age >= 40:
        print('вам следует обратиться к врачу!')
    else:
        print('вам следует заняться собой!')
#Остальные варианты
else:
    print('у вас интересный случай')
