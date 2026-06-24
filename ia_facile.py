import random

class EasyAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self, board):
# récuperation toutes les cases vides
        empty_cells = [
            i for i in range(9)
            if board.cells[i] == ""
        ]

        if empty_cells:
            return random.choice(empty_cells)

        return None