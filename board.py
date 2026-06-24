class Board:
    def __init__(self):
        self.cells = [""] * 9

    def display(self):
        for i in range(3):
            print(self.cells[i*3:(i+1)*3])

    def place_piece(self, position, player):
        if self.cells[position] == "":
            self.cells[position] = player
            return True
        return False

    def move_piece(self, start, end, player):
        if (
            self.cells[start] == player
            and self.cells[end] == ""
        ):
            self.cells[start] = ""
            self.cells[end] = player
            return True
        return False

    def check_winner(self):
        wins = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for combo in wins:
            a,b,c = combo

            if (
                self.cells[a] != ""
                and self.cells[a] == self.cells[b] == self.cells[c]
            ):
                return self.cells[a]

        return None