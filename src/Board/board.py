from src.Board.cell import Cell


class Board:
    def __init__(self, lines, columns, emptyValue = 0):
        self._lines = lines
        self._columns = columns
        self._value = emptyValue

        self._cells = self.createBoard()

    def createBoard(self):
        return [[Cell(line, column, self._value) for column in range(self._lines)] for line in range(self._columns)]

    def setValue(self, line, column, value):
        self._cells[line][column].value = value

    def getValuesFromLine(self, line):
        return [self._cells[line][column].value for column in range(self._columns)]

    def getValuesFromColumn(self, column):
        return [self._cells[line][column].value for line in range(self._lines)]

    def getValuesFromPrincipalDiagonal(self, line, column):
        array = []
        while line < self._lines and column < self._columns:
            array.append(self._cells[line][column].value)
            line += 1
            column += 1
        return array

    def getValuesFromSecundalDiagonal(self, line, column):
        array = []
        while line < self._lines and column > 0:
            array.append(self._cells[line][column].value)
            line += 1
            column -= 1
        return array

    def getAllCells(self):
        return [[self._cells[line][column] for line in range(self._lines)] for column in range(self._columns)]

    def getEmptyCells(self):
        """
        Function finds all empty cells and returns them in a list
        :return: a list of empty cells
        """
        array = []
        for line in range(self._lines):
            for column in range(self._columns):
                if self._cells[line][column].value == self._value:
                    array.append(self._cells[line][column])
        return array

    def __str__(self):
        arrayString = '  '
        for column in range(self._lines):
            if column < 9:
                arrayString = arrayString + ' '
            arrayString = arrayString + '  ' + str(column + 1)
        arrayString = arrayString + '\n'

        for line in range (self._lines):
            if line < 9:
                arrayString = arrayString + ' '
            arrayString = arrayString + str(line + 1)
            for column in range(self._columns):
                if self._cells[line][column].value == 0:
                    arrayString = arrayString + '   +'
                else:
                    arrayString = arrayString + '   ' + str(self._cells[line][column].value)
            arrayString = arrayString + '\n'
        return arrayString

if __name__ == '__main__':
    board = Board(15, 15)
    print(board.__str__())
