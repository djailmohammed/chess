from models.pieces import *
from config import BOARD_SIZE

class Board:
    """
    Represents the chess board and holds the state of all pieces.
    The board is stored as a 2D list (grid) indexed as grid[row][col]
    """
    def __init__(self):
        """
        Creates an empty BOARD_SIZE x BOARD_SIZE grid and initializes
        all chess pieces in their starting positions.
        """
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.initialize_pieces()

    def initialize_pieces(self):
        """
        Places all chess pieces on the board in their standard
        starting positions.
        """
        for col in range(BOARD_SIZE):
            self.grid[1][col] = Pawn("black", (1, col))
            self.grid[6][col] = Pawn("white", (6, col))

        self.grid[0][1] = Knight("black", (0, 1))
        self.grid[0][6] = Knight("black", (0, 6))
        self.grid[7][1] = Knight("white", (7, 1))
        self.grid[7][6] = Knight("white", (7, 6))

        self.grid[0][2] = Bishop("black", (0, 2))
        self.grid[0][5] = Bishop("black", (0, 5))
        self.grid[7][2] = Bishop("white", (7, 2))
        self.grid[7][5] = Bishop("white", (7, 5))

        self.grid[0][0] = Rook("black", (0, 0))
        self.grid[0][7] = Rook("black", (0, 7))
        self.grid[7][0] = Rook("white", (7, 0))
        self.grid[7][7] = Rook("white", (7, 7))

        self.grid[0][3] = Queen("black", (0, 3))
        self.grid[7][3] = Queen("white", (7, 3))

        self.grid[0][4] = King("black", (0, 4))
        self.grid[7][4] = King("white", (7, 4))

