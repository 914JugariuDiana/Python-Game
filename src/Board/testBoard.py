import unittest

from src.Board.board import Board
from src.Board.cell import Cell


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(5, 5)

    def tearDown(self) -> None:
        pass

    def testSetValue_correctCoordinates_ValueOfCell(self):
        self.board.setValue(4, 3, 1)
        self.assertEqual(self.board._cells[4][3].value, 1)

    def testGetValuesFromLine_correctLine_listContainingValuesFromLine(self):
        self.board.setValue(4, 3, 1)
        self.assertEqual(self.board.getValuesFromLine(4), [0, 0, 0, 1, 0])

    def testGetValuesFromColumn_correctColumn_listContainingValuesFromColumn(self):
        self.board.setValue(4, 3, 1)
        self.assertEqual(self.board.getValuesFromColumn(3), [0, 0, 0, 0, 1])

    def testGetValuesFromPrincipalDiagonal_correctCoordinates_listContainingValuesFromDiagonal(self):
        self.board.setValue(4, 3, 1)
        self.assertEqual(self.board.getValuesFromPrincipalDiagonal(1, 0), [0, 0, 0, 1])

    def testGetValuesFromSecundalDiagonal_correctCoordinates_listContainingValuesFromDiagonal(self):
        self.board.setValue(4, 3, 1)
        self.assertEqual(self.board.getValuesFromSecundalDiagonal(3, 4), [0, 1])

    def testGetEmptyCells_nothing_listContainingAllTheEmptyCells(self):
        self.board.setValue(1, 1, 1)
        self.board.setValue(4, 2, 1)
        self.board.setValue(4, 1, 1)
        self.board.setValue(4, 3, 1)
        self.board.setValue(3, 3, 1)
        self.board.setValue(2, 3, 1)
        self.board.setValue(3, 1, 1)
        self.board.setValue(2, 4, 1)
        self.board.setValue(0, 3, 1)
        self.board.setValue(1, 3, 1)
        list = [Cell(0, 0, 0), Cell(0, 1, 0), Cell(0, 2, 0), Cell(0, 4, 0), Cell(1, 0, 0), Cell(1, 2, 0), Cell(1, 4, 0),
                Cell(2, 0, 0), Cell(2, 1, 0), Cell(2, 2, 0), Cell(3, 0, 0), Cell(3, 2, 0), Cell(3, 4, 0), Cell(4, 0, 0),
                Cell(4, 4, 0)]
        self.assertEqual(self.board.getEmptyCells(), list)

