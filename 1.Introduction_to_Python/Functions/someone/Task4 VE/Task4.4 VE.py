#4: Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле

player = {
    "name": "name",
    "health": 100,
    "damage": 50,
    "armor": 1.2
}

enemy = {
    "name": "name",
    "health": 100,
    "damage": 50,
    "armor": 1.2
}

player["name"] = input("Введите имя игрока: ")
enemy["name"] = input("Введите имя противника: ")
player["damage"] = int(input("Введите урон игрока: "))
enemy["armor"] = float(input("Введите мультипликатор брони противника: "))

def damage(person1, person2):
    person1["damage"] = person1["damage"]/person2["armor"]
    return person1["damage"]

def attack (person1, person2, function):
    function(person1, person2)
    person2["health"] = person2["health"] - person1["damage"]
    return person2["health"]

print("{} наносит удар".format(player["name"]))
attack(player, enemy, damage)
if enemy["health"] > 0:
    print("У {} осталось {} HP".format(enemy["name"], round(enemy["health"], 1)))
else:
    print("{} повержен".format(enemy["name"]))