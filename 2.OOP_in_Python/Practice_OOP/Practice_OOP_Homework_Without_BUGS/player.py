from random import randint, choice


class Player:
    health = 10
    max_health = 10
    position = [0, 0]

    def __init__(self, position):
        self.position = position

    def was_hit(self, hid):
        self.health -= choice(range(hid))

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player's health", self.health)