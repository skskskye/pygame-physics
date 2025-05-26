import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def pointBetween(self, other):
        return Vector2(other.x - self.x, other.y - self.y)

    def mult(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def abs(self):
        return Vector2(abs(self.x), abs(self.y))

    def div(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def norm(self):
        return self.div(self.magnitude())
