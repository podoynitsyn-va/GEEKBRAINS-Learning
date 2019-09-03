from random import randint, choice


class Hamster:
    position = [0, 0]
    health = 3

    def __init__(self, hid, map_width, map_height, map):
        self.id = hid
        self.health = 2
        self.position = self.get_clear_posiion(map, map_width, map_height)

    def on_shot(self):
        self.health -=1
        return  self.health == 0

    def get_clear_posiion(self, map, map_width, map_heigth):
        while True:
            coords = [randint(0, map_width-1), randint(0, map_heigth-1)]
            if map.split("\n")[coords[1]] [coords[0]] == "*":
                return coords
