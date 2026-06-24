from board import Board


class Game:

    def __init__(self):
        self.board = Board()

        self.current_player = "X"

        self.phase = "placement"

        self.placed_X = 0
        self.placed_O = 0

    def switch_player(self):

        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def place(self, position):

        if self.board.place_piece(position, self.current_player):

            if self.current_player == "X":
                self.placed_X += 1
            else:
                self.placed_O += 1

            winner = self.board.check_winner()

            if winner:
                return winner

            if self.placed_X == 3 and self.placed_O == 3:
                self.phase = "movement"

            self.switch_player()

        return None