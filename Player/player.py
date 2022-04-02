from abc import abstractmethod

from src.Board.cell import Cell


class Player:
    def __init__(self, name, board):
        self._name = name
        self._board = board

    @abstractmethod
    def move(self, *arguments):
        pass

    def validateMove(self, line, column):
        """
        Function validates the coordinates of a move
        :param line: line of the move
        :param column: column of the move
        :return: True if we have a valid move, else False
        """
        if line < self._board._lines and line >= 0 and column < self._board._columns and column >= 0 and self._board._cells[line][column].value == 0:
            return True
        return False
