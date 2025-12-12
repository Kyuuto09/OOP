class Money:
    def __init__(self, major: int = 0, minor: int = 0):
        """
        major : whole currency units (dollars, euros, hryvnias)
        minor : cents...
        """
        self.set_value(major, minor)

    def set_value(self, major: int, minor: int):
        if minor >= 100:
            major += minor // 100
            minor = minor % 100

        if major < 0 or minor < 0:
            raise ValueError("Money values cannot be negative")

        self.major = major
        self.minor = minor

    def get_value(self):
        return self.major, self.minor

    def __str__(self):
        """Friendly formatted money output."""
        return f"{self.major}.{self.minor:02d}"

    def decrease(self, major: int = 0, minor: int = 0):
        total_cents = self.major * 100 + self.minor
        decrease_cents = major * 100 + minor

        if decrease_cents > total_cents:
            raise ValueError("Cannot decrease: price would become negative")

        new_total = total_cents - decrease_cents
        self.major = new_total // 100
        self.minor = new_total % 100


class Product:
    def __init__(self, name: str, price: Money):
        self.name = name
        self.price = price

    def reduce_price(self, major: int = 0, minor: int = 0):
        self.price.decrease(major, minor)

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"