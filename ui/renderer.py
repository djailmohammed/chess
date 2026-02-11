import os.path

import pygame

from config import LIGHT_SQUARE, DARK_SQUARE, SQUARE_SIZE, BOARD_SIZE, ASSETS_DIR
from models.board import Board
from models.pieces import Piece

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.piece_images = {}

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE

                rect = pygame.Rect(
                    SQUARE_SIZE * col,
                    SQUARE_SIZE * row,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )

                pygame.draw.rect(self.screen, color, rect)

    def draw_pieces(self, board: Board, dragging_piece=None):
        for row_idx, row in enumerate(board.grid):
            for col_idx, piece in enumerate(row):
                if piece and piece != dragging_piece:
                    piece_image = self.get_piece_image(piece)

                    x = col_idx * SQUARE_SIZE
                    y = row_idx * SQUARE_SIZE

                    self.screen.blit(piece_image, (x, y))

    def draw_dragging_piece(self, piece, mouse_pos):
        if piece and mouse_pos:
            piece_image = self.get_piece_image(piece)

            # Center on mouse
            rect = piece_image.get_rect(center=mouse_pos)
            self.screen.blit(piece_image, rect)

    def draw_mouse_highlight(self, position):
        if position:
            col = position[0] // SQUARE_SIZE
            row = position[1] // SQUARE_SIZE

            rect = pygame.Rect(
                col * SQUARE_SIZE,
                row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )

            border_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            pygame.draw.rect(border_surface, (245, 248, 250, 180), border_surface.get_rect(), 4)
            self.screen.blit(border_surface, rect)

    def draw_highlight(self, position):
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

    def get_piece_image(self, piece: Piece):
        key = f"{piece.color}-{piece.piece_type}"

        if key in self.piece_images:
            return self.piece_images[key]

        image_path = os.path.join(ASSETS_DIR, f"{key}.png")
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.smoothscale(image, (SQUARE_SIZE, SQUARE_SIZE))

        self.piece_images[key] = image

        return image

