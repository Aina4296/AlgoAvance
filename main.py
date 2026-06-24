from game import Game

game = Game()

while True:

    game.board.display()

    pos = int(
        input(
            f"Joueur {game.current_player} position (0-8): "
        )
    )

    winner = game.place(pos)

    if winner:
        print(f"Victoire de {winner}")
        break