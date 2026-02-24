# Mouse/Pygame → Grid
# col = mouse_x // SQUARE_SIZE   # x → col (horizontal)
# row = mouse_y // SQUARE_SIZE   # y → row (vertical)
#
# Grid → Mouse/Pygame
# x = col * SQUARE_SIZE          # col → x (horizontal)
# y = row * SQUARE_SIZE          # row → y (vertical)

import os.path

import pygame
import pygame.gfxdraw

from config import LIGHT_SQUARE, DARK_SQUARE, SQUARE_SIZE, BOARD_SIZE, ASSETS_DIR
from models.board import Board
from models.pieces import Piece

class Renderer:
    """
    Handles all visual rendering of the board, pieces, and highlights.
    This class does not modify game state.
    """
    def __init__(self, screen: pygame.Surface):
        """
        Initializes the renderer.

        :param screen: The pygame display surface to draw on.
        """
        self.screen = screen
        self.piece_images = {}

    def draw_board(self):
        """
        Draws the chessboard background using alternating light
        and dark squares.
        """
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE

                rect = pygame.Rect(
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )

                pygame.draw.rect(self.screen, color, rect)

    def draw_pieces(self, board: Board, dragging_piece: Piece = None):
        """
        Draws all pieces currently on the board except the piece
        being dragged (if any).

        :param board: The Board instance containing piece positions.
        :param dragging_piece: The piece currently being dragged by the mouse.
        """
        for row, row_data in enumerate(board.grid):
            for col, piece in enumerate(row_data):
                if piece and piece != dragging_piece:
                    piece_image = self.get_piece_image(piece)

                    x = col * SQUARE_SIZE
                    y = row * SQUARE_SIZE

                    self.screen.blit(piece_image, (x, y))

    def draw_dragging_piece(self, piece: Piece, mouse_pos: tuple[int, int]):
        """
        Draws the piece currently being dragged, centered on the mouse.

        :param piece: The piece being dragged.
        :param mouse_pos: Mouse position in screen coordinates (x, y).
        """
        if piece and mouse_pos:
            piece_image = self.get_piece_image(piece)

            # Center on mouse
            rect = piece_image.get_rect(center=mouse_pos)
            self.screen.blit(piece_image, rect)

    def draw_mouse_highlight(self, mouse_pos: tuple[int, int]):
        """
        Draws a border highlight around the square currently
        under the mouse cursor.

        :param mouse_pos: Mouse position in screen coordinates (x, y).
        """
        if mouse_pos:
            col = mouse_pos[0] // SQUARE_SIZE
            row = mouse_pos[1] // SQUARE_SIZE

            # Snapping mouse to the closest square
            rect = pygame.Rect(
                col * SQUARE_SIZE,
                row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )

            border_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(border_surface, (245, 248, 250, 180), border_surface.get_rect(), 4)
            self.screen.blit(border_surface, rect)

    def draw_highlight(self, position: tuple[int, int]):
        """
        Draws a filled highlight on a specific board square.

        :param position: Board position as (row, col).
        """
        if position:
            row, col = position

            rect = pygame.Rect(
                col * SQUARE_SIZE,
                row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )

            # Transparent surface to use RGBA
            highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            highlight_surface.fill((108, 163, 196, 130))
            self.screen.blit(highlight_surface, rect)

    def draw_legal_moves(self, valid_moves):
        radius = SQUARE_SIZE // 7

        for row, col in valid_moves:
            circle_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)

            center = SQUARE_SIZE // 2

            # anti-aliased edge
            pygame.gfxdraw.aacircle(
                circle_surface,
                center,
                center,
                radius,
                (0, 0, 0, 100)
            )

            # filled circle
            pygame.gfxdraw.filled_circle(
                circle_surface,
                center,
                center,
                radius,
                (0, 0, 0, 100)
            )

            self.screen.blit(circle_surface, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def get_piece_image(self, piece: Piece) -> pygame.Surface:
        """
        Loads and caches the image for a given chess piece.

        :param piece: The piece whose image is requested.
        :return: A pygame Surface representing the piece image.
        """
        key = f"{piece.color}-{piece.piece_type}"

        if key in self.piece_images:
            return self.piece_images[key]

        image_path = os.path.join(ASSETS_DIR, f"{key}.png")

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Missing piece image: {image_path}")

        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.smoothscale(image, (SQUARE_SIZE, SQUARE_SIZE))

        self.piece_images[key] = image

        return image