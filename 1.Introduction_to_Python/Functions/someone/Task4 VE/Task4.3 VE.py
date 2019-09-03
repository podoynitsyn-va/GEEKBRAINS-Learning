#3: Надо создать функцию attack(person1, person2)

player = {
    "name": "name",
    "health": 100,
    "damage": 50
}

enemy = {
    "name": "name",
    "health": 100,
    "damage": 50
}

player["name"] = input("Введите имя игрока: ")
enemy["name"] = input("Введите имя противника: ")
player["damage"] = int(input("Введите урон игрока: "))

def attack (person1, person2):
    person2["health"] = person2["health"] - person1["damage"]
    return person2["health"]

print("{} наносит удар".format(player["name"]))
attack(player, enemy)
if enemy["health"] > 0:
    print("У {} осталось {} HP".format(enemy["name"], enemy["health"]))
else:
    print("{} повержен".format(enemy["name"]))