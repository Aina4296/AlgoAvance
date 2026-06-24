import tkinter as tk
from game import Game

class FanoronGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fanoron-telo")

        self.game = Game()

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
        winner = self.game.place(pos)

        self.update_board()

        if winner:
            self.label.config(text=f"Victoire de {winner}")
            self.disable_buttons()
        else:
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