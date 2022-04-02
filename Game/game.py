from src.Game.exceptions import InputError
from src.Player.human import Human


class Game:
    def __init__(self, player1, player2, board):
        self._board = board
        self._player1 = player1
        self._player2 = player2

    def play(self):
        gameStatus = True
        lineComputer = 0
        columnComputer = 0
        while gameStatus:
            try:
                gameStatus, line, column = self.move(self._player1, 1)
                if not gameStatus:
                    break
                gameStatus, line, column = self.move(self._player2, 2, line, column, lineComputer, columnComputer)
                lineComputer = line
                columnComputer = column
                if not gameStatus:
                   break
            except ValueError as ve:
                print("error -" + str(ve))
            except InputError as ie:
                print("error -" + str(ie))

    def move(self, player, value, *arguments):
        if type(player) is Human:
            print(self._board)
            line, column = self.readMove()
            self._player1.move(line, column, value)
            gameStatus = self.checkGameFinish(line, column, value)
            if not gameStatus:
                print(self._board)
                print("Game over! YOU WIN!\n   CONGRATS!!!")
            return gameStatus, line, column
        else:
            lineHuman, columnHuman, line, column = arguments
            line, column = self._player2.move(lineHuman, columnHuman, line, column, value)
            gameStatus = self.checkGameFinish(line, column, value)
            if not gameStatus:
                print(self._board)
                print("   Game over! Computer wins!\n   Nice try, maybe next time!")
            return gameStatus, line, column

    def readMove(self):
        read = True
        while read:
            print('Write next move:')
            print('<line> : ', end='')
            line = int(input())
            print('<column> : ', end='')
            column = int(input())
            """if line == int(line) and column == int(column):
                line = int(line)
                column = int(column)
            else:
                raise InputError"""
            if self._player1.validateMove(line - 1, column - 1) and read:
                read = False
                return line - 1, column - 1
            else:
                raise InputError


    def checkGameFinish(self, line, column, value):
        maximSubArray = 0
        position, lenght = Game.checkArray(self._board.getValuesFromLine(line), value)
        if lenght > maximSubArray:
            maximSubArray = lenght
        position, lenght = Game.checkArray(self._board.getValuesFromColumn(column), value)
        if lenght > maximSubArray:
            maximSubArray = lenght
        if line > column:
            position, lenght = Game.checkArray(self._board.getValuesFromPrincipalDiagonal(line - column, 0), value)
        else:
            position, lenght = Game.checkArray(self._board.getValuesFromPrincipalDiagonal(0, column - line), value)
        if lenght > maximSubArray:
            maximSubArray = lenght
        if line + column < self._board._lines:
            position, lenght = Game.checkArray(self._board.getValuesFromSecundalDiagonal(0, column + line), value)
        else:
            position, lenght = Game.checkArray(self._board.getValuesFromSecundalDiagonal(line + column - self._board._lines + 1, self._board._lines - 1), value)
        if lenght > maximSubArray:
            maximSubArray = lenght
        if maximSubArray == 5:
            return False
        return True

    @staticmethod
    def checkArray(array, value):
        """
        Functions receives an array and returns the beginning and the lenght of the maximum substring of given value
        :param array: the initial array
        :param value: the value of the elements we are looking for
        :return: the position before the beginning of the array
        """
        maximLenghtOfSameElementsArray = 0
        arrayBeggining = 0
        previousValue = 0
        currentLenght = 0
        cellNumber = -1
        for cellValue in array:
            cellNumber += 1
            if cellValue == previousValue and previousValue == value:
                currentLenght += 1
            else:
                if currentLenght > maximLenghtOfSameElementsArray and previousValue == value:
                    maximLenghtOfSameElementsArray = currentLenght
                    arrayBeggining = cellNumber - maximLenghtOfSameElementsArray
                currentLenght = 1
                previousValue = cellValue
        if currentLenght > maximLenghtOfSameElementsArray and previousValue == value:
            maximLenghtOfSameElementsArray = currentLenght

        return arrayBeggining - 1, maximLenghtOfSameElementsArray