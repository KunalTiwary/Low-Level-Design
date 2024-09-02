from .PlayingPiece import PlayingPiece


class Player:
    def __init__(self, name, playingPiece: PlayingPiece):
        self.name = name
        self.playingPiece = playingPiece

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_playingPiece(self):
        return self.playingPiece

    def set_playingPiece(self, playingPiece):
        self.playingPiece = playingPiece


