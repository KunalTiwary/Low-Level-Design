from .PieceType import PieceType
from .PlayingPiece import PlayingPiece


class PieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
