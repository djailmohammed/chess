from config import SQUARE_SIZE, BOARD_SIZE
from models.pieces import Piece


class InputHandler:
    def __init__(self):
        self.dragging_piece: Piece = None
        self.dragging_position = None
        self.mouse_pos = None

    def handle_mouse_down(self, pos, board):
        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE

        piece = board.grid[row][col]
        if piece:
            self.dragging_piece = piece
            self.dragging_position = (row, col)
            self.mouse_pos = pos

    def handle_mouse_up(self, pos, board):
        if self.dragging_piece is None:
            return

        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE

        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            old_row, old_col = self.dragging_position
            board.grid[old_row][old_col] = None

            board.grid[row][col] = self.dragging_piece
            self.dragging_piece.position = (row, col)

        self.dragging_piece = None
        self.dragging_position = None
        self.mouse_pos = None

    def handle_mouse_motion(self, pos):
        if self.dragging_piece:
            self.mouse_pos = pos

    def is_dragging(self):
        return self.dragging_piece is not None

    def get_dragging_info(self):
        return self.dragging_piece, self.mouse_pos, self.dragging_position