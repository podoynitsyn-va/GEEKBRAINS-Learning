# ТЗ 3 Угадайка
import random


user_number     = 0 #чтобы услвоие красивое работало
levels          = {1:15,2:10,3:5}
#Определим диапазон чисел для игры
#Ихже будем использовать для сужения диапазона
number_min = 1
number_max = 100
# Если true, то в двух последних попытках будем брать случайное число
panic_mode = True

user_answer = input("Привет! Поиграем в игру «угадай число»?\n"
      "Если ты мне доверяешь, я могу изолировать часть своего сознания и хранить загаданное число без необходимости держать его в голове?\n"
      "Изолировать часть сознания для хранения числа (Y/N или Д/Н)? :(Y)")
user_answer = user_answer.lower()

if user_answer == 'н' or user_answer == 'n':
    print("Хорошо, но тогда запомни своё число, и чур не обманывать :)")
else:
    while not (1 <= user_number <= 100):
        user_number=int(input(f'Отлично! Загадай целое число от {number_min} до {number_max}: '))

#print(user_number)

level = int(input(f'Задай номер уровня, на котором будем играть. 1 уровень = {levels[1]}, 2 уровень = {levels[2]}, 3 уровень = {levels[3]} : '))



number_count = 0
#Загадаем всегда случайное началльное, чтобы было интерснее
my_number = None
#Для правильной работы надо изменить диапазоны, чтобы не упустить 1 и 100
number_min -= 1
number_max += 1

print("\nОтлично, начинаем играть!\n\n")

while number_count < levels[level]:
    number_count += 1

    # Проверим не жульничает пользователь
    if (number_max - number_min) <= 1:
        print("Не хочу больше играть, ты жульничаешь :(")
        break

    #Загадаем число разным способом в зависимости от оставшихся попыток
    str_question = ''
    #print(f'Мин={number_min} Макс={number_max}')

    if (my_number == None) or ((levels[level] - number_count <= 1) and panic_mode):
        my_number = random.randint(number_min + 1, number_max - 1)
    else:
        my_number = number_max - (number_max - number_min) // 2

    #Ещё раз сюда вставим, чтобы пользователь видел панику :)
    if (levels[level] - number_count <= 1) and panic_mode:
        str_question = "Аааа... "

    print(f'Попытка №{number_count} (осталось {levels[level]-number_count})')
    str_question += f'Моё число {my_number}. Загаданное тобой (б)ольше, (м)еньше или (р)авно моему'
    if user_number != None:
        str_question += f' (подсказка, ты загадал {user_number})'

    str_question += '?: '

    #Узнаем у пользователя больше загаданое число или меньше
    number_check = None
    while not number_check in ['Б','М','Р']:
        number_check = input(str_question).upper()

    #Проверяем что делать, в последних двух попытках будем делать
    if number_check == 'Р':
        print("Ура, я выиграл!")
        break
    elif number_check == 'Б':
        number_min = my_number
    else:
        number_max = my_number
else:
    print("Ну вот... я проиграл :(")

