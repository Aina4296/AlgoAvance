import math

class HardAI:
    def __init__(self, symbol):
        self.symbol = symbol
        self.opponent = "X" if symbol == "O" else "O"

    # Fonction d'évaluation simple
    def evaluate(self, board):

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

            if board.cells[a] == board.cells[b] == board.cells[c]:

                if board.cells[a] == self.symbol:
                    return 10
                elif board.cells[a] == self.opponent:
                    return -10

        return 0

    def is_moves_left(self, board):
        return "" in board.cells

    # MINIMAX + ALPHA BETA
    def minimax(self, board, depth, is_max, alpha, beta):

        score = self.evaluate(board)

        if score == 10 or score == -10:
            return score

        if not self.is_moves_left(board):
            return 0

        if is_max:
            best = -math.inf

            for i in range(9):
                if board.cells[i] == "":
                    board.cells[i] = self.symbol

                    best = max(
                        best,
                        self.minimax(board, depth+1, False, alpha, beta)
                    )

                    board.cells[i] = ""

                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

            return best

        else:
            best = math.inf

            for i in range(9):
                if board.cells[i] == "":
                    board.cells[i] = self.opponent

                    best = min(
                        best,
                        self.minimax(board, depth+1, True, alpha, beta)
                    )

                    board.cells[i] = ""

                    beta = min(beta, best)

                    if beta <= alpha:
                        break

            return best

    def choose_move(self, board):

        best_val = -math.inf
        best_move = None

        for i in range(9):

            if board.cells[i] == "":

                board.cells[i] = self.symbol

                move_val = self.minimax(
                    board,
                    0,
                    False,
                    -math.inf,
                    math.inf
                )

                board.cells[i] = ""

                if move_val > best_val:
                    best_move = i
                    best_val = move_val

        return best_move