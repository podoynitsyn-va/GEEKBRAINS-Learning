my_list_1 = [2, 2, 5, 12, 8, 2, 12]
new_list = []
for unic in my_list_1:
    if my_list_1.count(int(unic)) == 1:
        new_list.append(unic)
print(new_list)
