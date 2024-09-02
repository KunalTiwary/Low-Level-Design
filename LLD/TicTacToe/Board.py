from .PieceType import PieceType


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[-1 for _ in range(size)] for _ in range(size)]

    def addPiece(self, row, col, pieceType: PieceType):
        if self.board[row][col] != -1:
            return False
        self.board[row][col] = pieceType
        return True

    def returnFreeCells(self):
        freeCells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -1:
                    freeCells.append((i, j))
        return freeCells




