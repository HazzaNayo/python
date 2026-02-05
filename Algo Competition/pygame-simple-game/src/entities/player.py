class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def reset(self):
        self.health = 100
        self.x = 0
        self.y = 0