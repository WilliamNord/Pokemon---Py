class Move():
    def __init__(self, name: str , element: str, dmg_category: str, power: int, accuracy: int, priority: int):
        self.name = name
        self.element = element
        self.dmg_category = dmg_category
        self.power = power
        self.accuracy = accuracy
        self.priority = priority