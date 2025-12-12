class Airplane:
    def __init__(self, plane_type: str, max_passengers: int, current_passengers: int = 0):
        if max_passengers < 0 or current_passengers < 0:
            raise ValueError("Passenger numbers cannot be negative")
        if current_passengers > max_passengers:
            raise ValueError("Current passengers cannot exceed max capacity")

        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.plane_type == other.plane_type


    def __lt__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.max_passengers >= other.max_passengers

    def __add__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        new_passengers = self.current_passengers + value
        if new_passengers > self.max_passengers:
            raise ValueError("Too many passengers for this airplane")
        return Airplane(self.plane_type, self.max_passengers, new_passengers)

    def __sub__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        new_passengers = self.current_passengers - value
        if new_passengers < 0:
            raise ValueError("Passengers cannot become negative")
        return Airplane(self.plane_type, self.max_passengers, new_passengers)

    def __iadd__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        if self.current_passengers + value > self.max_passengers:
            raise ValueError("Too many passengers for this airplane")
        self.current_passengers += value
        return self

    def __isub__(self, value):
        if not isinstance(value, int):
            return NotImplemented
        if self.current_passengers - value < 0:
            raise ValueError("Passengers cannot become negative")
        self.current_passengers -= value
        return self

    def __str__(self):
        return f"Airplane(type={self.plane_type}, passengers={self.current_passengers}/{self.max_passengers})"
