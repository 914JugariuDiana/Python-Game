import random
from src.Player.player import Player
from src.Game.game import Game


class Computer(Player):
    def move(self, linePlayer, columnPlayer, line, column, value):
        """
        Program receives the coordinates of the last moves made, then finds a new set of coordinates and makes a new move
         which he returns.
        :param linePlayer: The last line on which the player made a move
        :param columnPlayer: The last column on which the player made a move
        :param line: The last line on which the computer made a move
        :param column: The last column on which the computer made a move
        :param value: the value which appears on the board
        :return: the coordinates of the new move
        """
        keepPreviosCoordinates = False
        newMove, lenght = self.lookForMove(linePlayer, columnPlayer, 1)
        if lenght < 3:
            newMove, lenght = self.lookForMove(line, column, value)
        else:
            if newMove != [-1, -1]:
                keepPreviosCoordinates = True
        if newMove == [-1, -1]:
            newCell = random.choice(self._board.getEmptyCells())
            newMove = [newCell.line, newCell.column]
        self._board.setValue(newMove[0], newMove[1], value)
        if keepPreviosCoordinates:
            return line, column
        return newMove[0], newMove[1]

    def lookForMove(self, line, column, value):
        """
        Function receives coordinates and looks for a move around the given position
        :param line: the line on which we look for a new move
        :param column: the column on which we look for a new move
        :param value: the value the computer tries to block
        :return: the coordinates of a possible new move and the maximum lenght of an array of value
        """
        maximSubArray = 0
        movePosition = [-1, -1]
        position, lenght = Game.checkArray(self._board.getValuesFromLine(line), value)
        if lenght >= maximSubArray or movePosition == [-1, -1]:
            maximSubArray = lenght
            movePosition = self.getMovePosition(line, position, lenght, 1)
        position, lenght = Game.checkArray(self._board.getValuesFromColumn(column), value)
        if lenght >= maximSubArray or movePosition == [-1, -1]:
            maximSubArray = lenght
            movePosition = self.getMovePosition(position, column, lenght, 2)
        if line > column:
            position, lenght = Game.checkArray(self._board.getValuesFromPrincipalDiagonal(line - column, 0), value)
            diagonalLine = line - column
            diagonalColumn = 0
        else:
            position, lenght = Game.checkArray(self._board.getValuesFromPrincipalDiagonal(0, column - line), value)
            diagonalLine = 0
            diagonalColumn = column - line
        if lenght >= maximSubArray or movePosition == [-1, -1]:
            maximSubArray = lenght
            movePosition = self.getMovePosition(diagonalLine + position, diagonalColumn + position, lenght, 3)
        if line + column < 15:
            position, lenght = Game.checkArray(self._board.getValuesFromSecundalDiagonal(0, column + line), value)
            diagonalLine = 0
            diagonalColumn = column + line
        else:
            position, lenght = Game.checkArray(self._board.getValuesFromSecundalDiagonal(line + column - 14, 14), value)
            diagonalLine = line + column - 14
            diagonalColumn = 14
        if lenght >= maximSubArray or movePosition == [-1, -1]:
            maximSubArray = lenght
            movePosition = self.getMovePosition(diagonalLine + position, diagonalColumn - position, lenght, 4)
        return movePosition, maximSubArray

    def getMovePosition(self, line, column, lenght, move):
        """
        Function tries to find a possible set of coordinates around the string with coordinates (line, column) for the
        first position and given lenght
        :param line: coordinate of a possible move
        :param column: coordinate of a possible move
        :param lenght: the lenght of the string
        :param move: where we look for a move(a line/column/diagonal)
        :return: a set of available coordinates if found, else [-1, -1]
        """
        if super().validateMove(line, column) and self._board._cells[line][column].value == 0:
            return [line, column]
        if move == 1:
            if super().validateMove(line, column + lenght + 1) and \
                    self._board._cells[line][column + lenght + 1].value == 0:
                return [line, column + lenght + 1]
        elif move == 2:
            if super().validateMove(line + lenght + 1, column) and \
                    self._board._cells[line + lenght + 1][column].value == 0:
                return [line + lenght + 1, column]
        elif move == 3:
            if super().validateMove(line + lenght + 1, column + lenght + 1) and \
                    self._board._cells[line + lenght + 1][column + lenght + 1].value == 0:
                return [line + lenght + 1, column + lenght + 1]
        elif move == 4:
            if super().validateMove(line + lenght + 1, column - lenght - 1) and \
                    self._board._cells[line + lenght + 1][column - lenght - 1].value == 0:
                return [line + lenght + 1, column - lenght - 1]
        return [-1, -1]
