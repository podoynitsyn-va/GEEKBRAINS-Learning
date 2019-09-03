#4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)


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
    damage_thr_armor = armor(attacks['damage'])
    damage_done = is_attacked['health'] - damage_thr_armor
    is_attacked['health'] = damage_done

def armor(damage):
    return int(damage) / 1.2


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
    print('{} strikes {}. {} health is now {}'.format(name, enemy['player'],enemy['player'], round((enemy['health']),2)))
else:
    player_attacked(enemy, player)
    print("{} strikes {}. {} health is now {}".format(enemy['player'], name, name, round((player['health']), 2)))