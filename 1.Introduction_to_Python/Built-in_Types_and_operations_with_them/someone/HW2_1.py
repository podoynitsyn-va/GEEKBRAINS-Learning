#1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# Примечание. Списки создайте вручную, например так:
#my_list_1 = [2, 5, 8, 2, 12, 12, 4]
#my_list_2 = [2, 7, 12, 3]

my_list_1 = input('Введите 1-ый список чисел: ')
my_list_2 = input('Введите 2-ой список чисел: ')
my_list_1 = set(my_list_1.split())
print(my_list_1)
my_list_2 = set(my_list_2.split())
print(my_list_2)
print(my_list_1 - my_list_2)