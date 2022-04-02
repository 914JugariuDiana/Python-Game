from src.Board.board import Board
from src.Game.game import Game
from src.Player.computer import Computer
from src.Player.human import Human

if __name__ == '__main__':
    board = Board(15, 15)
    player1 = Human('human', board)
    player2 = Computer('computer', board)
    game = Game(player1, player2, board)

    game.play()