from abc import ABC, abstractmethod

from config import BOARD_SIZE


class Piece(ABC):
    piece_type = "piece"

    def __init__(self, color, position):
        self.color = color
        self.position = position

    @abstractmethod
    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        pass


class Pawn(Piece):
    piece_type = "pawn"

    def __init__(self, color, position):
        super().__init__(color, position)

    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        moves = []
        row, col = self.position
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        new_row = row + direction

        if 0 <= new_row < BOARD_SIZE and grid[new_row][col] is None:
            moves.append((new_row, col))
            if row == start_row:
                new_row2 = row + (2 * direction)
                if grid[new_row2][col] is None:
                    moves.append((new_row2, col))

        for dc in [-1, 1]:
            new_col = col + dc
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
                capture = grid[new_row][new_col]
                if capture and capture.color != self.color:
                    moves.append((new_row, new_col))

        return moves


class Knight(Piece):
    piece_type = "knight"

    def __init__(self, color, position):
        super().__init__(color, position)

    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        pass


class Bishop(Piece):
    piece_type = "bishop"

    def __init__(self, color, position):
        super().__init__(color, position)

    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        pass


class Rook(Piece):
    piece_type = "rook"

    def __init__(self, color, position):
        super().__init__(color, position)

    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        pass


class Queen(Piece):
    piece_type = "queen"

    def __init__(self, color, position):
        super().__init__(color, position)

    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        pass


class King(Piece):
    piece_type = "king"

    def __init__(self, color, position):
        super().__init__(color, position)

    def get_valid_moves(self, grid) -> list[tuple[int, int]]:
        pass


