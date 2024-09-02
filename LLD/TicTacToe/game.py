from collections import deque
from .Board import Board
from .Player import Player
from .PieceX import PieceX
from .PieceO import PieceO


class TicTacToe:

    def __init__(self):
        self.players = deque()
        self.gameBoard = Board(3)
        crossPiece = PieceX()
        self.player1 = Player("Player1", crossPiece)
        noughtsPiece = PieceO()
        self.player2 = Player("Player2", noughtsPiece)
        self.players.append(self.player1)
        self.players.append(self.player2)

    def startGame(self):
        noWinner = True
        while noWinner:
            playerTurn = self.players.popleft()
            freeCells = self.gameBoard.returnFreeCells()


