import random


def rand_list_element(my_list):
    if not my_list:
        return None
    else:
        return random.choice(my_list)

#
# new_list = [1, 2, 3, 4, 5]
# print(rand_list_element(new_list))
