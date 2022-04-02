from src.Board.cell import Cell
from src.Player.player import Player


class Human(Player):
    def move(self, line, column, value):
        self._board.setValue(line, column, value)
