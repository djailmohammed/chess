class Piece:
    piece_type = "piece"

    def __init__(self, color, position):
        self.color = color
        self.position = position


class Pawn(Piece):
    piece_type = "pawn"

    def __init__(self, color, position):
        super().__init__(color, position)


class Knight(Piece):
    piece_type = "knight"

    def __init__(self, color, position):
        super().__init__(color, position)


class Bishop(Piece):
    piece_type = "bishop"

    def __init__(self, color, position):
        super().__init__(color, position)


class Rook(Piece):
    piece_type = "rook"

    def __init__(self, color, position):
        super().__init__(color, position)


class Queen(Piece):
    piece_type = "queen"

    def __init__(self, color, position):
        super().__init__(color, position)


class King(Piece):
    piece_type = "king"

    def __init__(self, color, position):
        super().__init__(color, position)


