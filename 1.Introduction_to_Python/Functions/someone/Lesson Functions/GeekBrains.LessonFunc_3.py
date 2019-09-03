#3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#name - строка полученная от пользователя,
#health = 100,
#damage = 50.
# ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

import random
name = input('Enter your name: ')
enemy_health_gen = random.randint(200, 500)
enemy_damage_gen = random.randint(10, 20)
player = {'player':name,
            'health':100,
            'damage':50}
enemy = {'player': 'Thanos',
             'damage': enemy_damage_gen,
             'health': enemy_health_gen}

print('Game start:')
print('{}! You have {} health points, and you deal {} damage!'.format(name,player['health'],player['damage']))
print('Your enemy is {}! He has {} health points, and can deal {} damage!'.format(enemy['player'],enemy['health'],enemy['damage']))

def player_attacked(attacks, is_attacked):
    damage_done = is_attacked['health'] - attacks['damage']
    is_attacked['health'] = damage_done

roll = input('Type r to see who strikes first: ')
move_gen = random.randint(0,100)

while roll == 'r':
    result =[]
    if  move_gen >= 50:
        print('{} strikes first!'.format(name))
        result.append(name)
    else:
        print('{} strikes first!'.format(enemy['player']))
        result.append(enemy['player'])
    break

if  name in result:
    player_attacked(player, enemy)
    print('{} strikes {}. {} health is now {}'.format(name,enemy['player'],enemy['player']),enemy['health'])
else:
    player_attacked(enemy, player)
    print('{} strikes {}. {} health is now {}'.format(enemy['player'],name,name,player['health']))



