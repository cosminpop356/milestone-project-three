from random import randint

class Board:
    """
    Creates an instance of Board
    """
    
    def __init__(self, size, name, num_ships, type):
        self.size = size
        self.name = name
        self.num_ships = num_ships
        self.type = type
        self.board = [["[]" for x in range(size)] for y in range(size)]


