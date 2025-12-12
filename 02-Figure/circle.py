import math

class Circle:
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    # ---------- Helper part--------
    def circumference(self):
        return 2 * math.pi * self.radius

    # ---------- Equality part---------
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    # ---------- Comparisons part ----------
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.circumference() < other.circumference()

    def __le__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.circumference() <= other.circumference()

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.circumference() > other.circumference()

    def __ge__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.circumference() >= other.circumference()

    # ---------- Arithmetic part ----------
    def __add__(self, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        return Circle(self.radius + value)

    def __sub__(self, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        new_r = self.radius - value
        if new_r < 0:
            raise ValueError("Radius cannot become negative")
        return Circle(new_r)

    def __iadd__(self, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        self.radius += value
        return self

    def __isub__(self, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        if self.radius - value < 0:
            raise ValueError("Radius cannot become negative")
        self.radius -= value
        return self

    def __str__(self):
        return f"Circle(radius={self.radius})"

