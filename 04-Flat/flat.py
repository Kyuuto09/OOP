class Flat:
    def __init__(self, area: float, price: float):
        if area <= 0:
            raise ValueError("Area must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")

        self.area = area
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.area == other.area

    def __ne__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.area != other.area

    def __lt__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        if not isinstance(other, Flat):
            return NotImplemented
        return self.price >= other.price

    def __str__(self):
        return f"Flat(area={self.area} m², price={self.price}$)"
