from config import SQUARE_SIZE, BOARD_SIZE
from models.board import Board
from models.pieces import Piece


class InputHandler:
    """
    Handles mouse input and drag-and-drop interactions for chess pieces.

    This class tracks the currently dragged piece, its original board
    position, and the current mouse position.
    """
    def __init__(self):
        """
        Initializes input state with no active drag operation.
        """
        self.dragging_piece: Piece = None
        self.dragging_origin: tuple[int, int] = None
        self.mouse_pos: tuple[int, int] = None
        self.selected_piece: Piece = None
        self.selected_origin: tuple[int, int] = None

    def handle_mouse_down(self, mouse_pos: tuple[int, int], board: Board):
        """
        Handles left mouse button press.

        If a piece exists at the clicked board square, it becomes the
        currently dragged piece.

        :param mouse_pos: Mouse position in screen coordinates (x, y).
        :param board: The Board instance containing the game state.
        """

        col = mouse_pos[0] // SQUARE_SIZE
        row = mouse_pos[1] // SQUARE_SIZE
        clicked_pos = (row, col)

        piece = board.grid[row][col]

        if piece and  self.selected_piece == piece and self.selected_origin == clicked_pos:
            self.selected_piece = None
            self.selected_origin = None

        if piece:
            self.dragging_piece = piece
            self.dragging_origin = clicked_pos
            self.selected_piece = piece
            self.selected_origin = clicked_pos
            self.mouse_pos = mouse_pos

    def handle_mouse_up(self, mouse_pos: tuple[int, int], board: Board):
        """
        Handles left mouse button release.

        If a piece is being dragged, it is placed on the board square
        under the mouse cursor. Drag state is cleared afterward.

        :param mouse_pos: Mouse position in screen coordinates (x, y).
        :param board: The Board instance containing the game state.
        """
        if self.dragging_piece is None:
            return

        col = mouse_pos[0] // SQUARE_SIZE
        row = mouse_pos[1] // SQUARE_SIZE

        if 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE:
            # TODO: Move piece change logic and rules elsewhere (board or something else)
            old_row, old_col = self.dragging_origin
            board.grid[old_row][old_col] = None

            board.grid[row][col] = self.dragging_piece
            self.dragging_piece.position = (row, col)

        self.dragging_piece = None
        self.dragging_origin = None
        self.mouse_pos = None

    def handle_mouse_motion(self, mouse_pos: tuple[int, int]):
        """
       Updates the mouse position while a piece is being dragged.

       :param mouse_pos: Mouse position in screen coordinates (x, y).
       """
        if self.dragging_piece:
            self.mouse_pos = mouse_pos

    def is_dragging(self) -> bool:
        """
        Returns whether a piece is currently being dragged.

        :return: True if dragging a piece, False otherwise.
        """
        return self.dragging_piece is not None

    def is_selected(self) -> bool:
        """
        Returns whether a piece is currently being selected.

        :return: True a piece is selected, False otherwise.
        """
        return self.selected_piece is not None

    def get_dragging_info(self) -> tuple[
        Piece | None,
        tuple[int, int] | None,
        tuple[int, int] | None
    ]:
        """
        Returns information about the current drag operation.

        :return: A tuple containing:
                 - the dragged piece (or None),
                 - the current mouse position (x, y),
                 - the original board position (row, col).
        """
        return self.dragging_piece, self.mouse_pos, self.dragging_origin

    def get_selected_info(self):
        """Returns (piece, position) of selected piece."""
        return self.selected_piece, self.selected_origin