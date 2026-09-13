class Move():
    def __init__(self, name: str , element: str, power: int, accuracy: int, priority: int):
        self.name = name
        self.element = element
        self.power = power
        self.accuracy = accuracy
        self.priority = priority