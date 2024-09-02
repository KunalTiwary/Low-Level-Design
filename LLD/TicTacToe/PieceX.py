from .PieceType import PieceType
from .PlayingPiece import PlayingPiece


class PieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
