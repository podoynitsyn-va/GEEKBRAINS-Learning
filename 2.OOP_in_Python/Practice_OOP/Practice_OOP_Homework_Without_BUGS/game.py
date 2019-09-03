from player import Player
from hamsters import Hamster
from random import randint

hamsters_count = 4


class Game:

    map = ""
    map_width = 0
    map_heigth = 0
    game_one = True
    happy_message = "You WIN!!! Congratulations!!!"
    killed_hamsters = 0

    def __init__(self):
        self.generate_map()
        player_position = [randint(0, self.map_width-1), randint(0, self.map_heigth-1)]
        self.player = Player(player_position)
        self.hamsters = []
        for i in range (hamsters_count):
            self.hamsters.append(Hamster(i+1, self.map_width, self.map_heigth, self.get_full_map(), player_position))
        #self.hamsters = [Hamster(i+1, self.map_width, self.map_heigth) for i in range(hamsters_count)]

    def generate_map(self):
        x, y = [int(s) for s in input("Введите ширину и высоту карты через пробел: ").split()]
        s = ""
        for i in range(y):
            for j in range(x):
                s = s + "*"
            if i < y-1:
                s = s + "\n"
        self.map_width = x
        self.map_heigth = y
        self.map = s

    def add_point(self, position, name, s):
        li = s.split("\n")
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return "\n".join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, "X", s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        print(s)

    def move_player(self, destination):
        """destination = w,a,s,d"""
        if destination == "s":
            if self.player.position[1] == self.map_heigth - 1:
                return False
            self.player.position[1] +=1 # bottom
        if destination == "w":
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -=1 # top
        if destination == "a":
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -=1 # left
        if destination == "d":
            if self.player.position[0] == self.map_width - 1:
                return False
            self.player.position[0] +=1 # right
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split("\n")[coords[1]][coords[0]]

    directions = {"w":"s", "s":"w", "d":"a", "a":"d"}

    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        if not hamster == "*":
            self.player.was_hit(int(hamster))
            if self.player.health <=0:
                self.game_one = False
                print("you died... game over...")
                return False
            print("player's health: ", self.player.health)
            killed = self.hamsters[int(hamster)-1].on_shot()
            if not killed:
                print("wasn't killed!")
                self.move_player(self.directions[direction])
            else:
                print("hamster", self.hamsters[int(hamster)-1].id, "was killed!")
                self.hamsters[int(hamster) - 1].id = "*"
                self.killed_hamsters +=1

    def start(self):
        self.render_map()
        while self.game_one:
            if self.killed_hamsters == hamsters_count:
                print(self.happy_message)
                return True
            command = input("Insert command: ")
            if command in ["a", "s", "d", "w"]:
                self.move_player(command)
                self.render_map()
            if command == "q":
                self.game_one = False
                print("game over!")
            if command == "e":
                self.player.wait()


game = Game()
game.start()

"""
1. (не баг) сделана генерация карты по индексам, которые игрок вводит сам.
2. (не баг) в начале игры игрок рандомно размещается на поле.
3. (баг) хомяки могут размещаться на карте в начале игры в том же месте, что и игрок
    Как исправил:
        сделал размещение хомяков с учетом размещения игрока. Передаем координаты игрока при инициализации хомяка
        и при расчете get_clear_position в классе Hamster проверяем, чтобы координаты нового хомяка
        не совпадали с координатами уже созданных хомяков, и координатами игрока.
4. (баг/не баг) при выходе за границы поля - перемещения не происходит, возвращается False, игрок остаётся на месте.
5. (баг) если хомяки стояли рядом, и убив хомяка А, мы начинаем следующим шагом атаковать хомяка Б, возникает следующее:
    атака на хомяка Б
    хомяк Б ранен
    нас отбрасывает обратно
    но при отбросе мы попадаем на поле, где есть хомяк А.
    он не отображается, но он там есть, по координатам поля (как суслик в ДМБ)
    и нас отбрасывает обратно на хомяка Б.
    и так, пока какой-то из хомяков не помрёт или у нас не закончится здоровье.
    Влиять на это мы не можем, это происходит автоматически.
    Как исправил:
        Есть ли хомяк на поле - определяет метод get_hamster_on_position, возвращающий свойство "id" хомяка
        или символ "*", означающий незанятое поле.
        У убитого хомяка меняем значение свойства "id" на "*". 
        В итоге программа вместо хомяка видит пустое поле.
6. (баг) хорошая концовка не заканчивается, поскольку длина списка хомяков в процессе игры не изменяется
    Как исправил:
        завёл новое свойство killed_hamsters = 0 и при убийстве хомяка увеличивал его на 1
        если количество убитых хомяков killed_hamsters равно количеству хомяков в начале игры hamsters_count,
        тогда мы выиграли, ура!
"""