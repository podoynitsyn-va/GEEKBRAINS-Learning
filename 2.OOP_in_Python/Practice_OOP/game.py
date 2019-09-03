from player import Player
from hamsters import Hamster

hamsters_count = 4


class Game:
    map = ""
    map_width = 0
    map_heigth = 0
    game_one = True
    happy_message = "You WIN!!! Congratulations!!!"


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


    def __init__(self):
        self.generate_map()
        self.player = Player()
        self.hamsters = []
        for i in range (hamsters_count):
            self.hamsters.append(Hamster(i+1, self.map_width, self.map_heigth, self.get_full_map()))
        #self.hamsters = [Hamster(i+1, self.map_width, self.map_heigth) for i in range(hamsters_count)]


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

    def start(self):
        self.render_map()
        while self.game_one:
            if len(self.hamsters) == 0:
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