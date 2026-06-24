import tkinter as tk
from game import Game
from ia_facile import EasyAI


class FanoronGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fanoron-telo")

        self.game = Game()

        # IA facile (joue O)
        self.ai = EasyAI("O")
        self.human_vs_ai = True

        self.buttons = []

        self.create_board()

        self.label = tk.Label(
            root,
            text="Tour du joueur X",
            font=("Arial", 14)
        )
        self.label.pack()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame,
                text="",
                font=("Arial", 20),
                width=5,
                height=2,
                command=lambda i=i: self.click(i)
            )
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def click(self, pos):

        # Joueur humain (X)
        if self.game.current_player == "X":

            winner = self.game.place(pos)
            self.update_board()

            if winner:
                self.label.config(text=f"Victoire de {winner}")
                self.disable_buttons()
                return

            # Tour IA
            if self.human_vs_ai and self.game.current_player == "O":
                self.root.after(500, self.ai_play)

            self.label.config(
                text=f"Tour du joueur {self.game.current_player}"
            )

    def ai_play(self):

        move = self.ai.choose_move(self.game.board)

        if move is not None:
            winner = self.game.place(move)
            self.update_board()

            if winner:
                self.label.config(text=f"Victoire de {winner}")
                self.disable_buttons()
                return

        self.label.config(
            text=f"Tour du joueur {self.game.current_player}"
        )

    def update_board(self):
        for i in range(9):
            self.buttons[i].config(
                text=self.game.board.cells[i]
            )

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = FanoronGUI(root)
    root.mainloop()