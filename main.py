import pygame

from config import SQUARE_SIZE
from models.board import Board
from ui import renderer
from ui.input_handler import InputHandler

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

renderer_instance = renderer.Renderer(screen)
board = Board()
input_handler = InputHandler()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                input_handler.handle_mouse_down(event.pos, board)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                input_handler.handle_mouse_up(event.pos, board)

        if event.type == pygame.MOUSEMOTION:
                input_handler.handle_mouse_motion(event.pos)

        screen.fill((0, 0, 0))

        renderer_instance.draw_board()
        dragging_piece, mouse_pos, drag_origin = input_handler.get_dragging_info()
        renderer_instance.draw_pieces(board, dragging_piece)
        renderer_instance.draw_highlight(drag_origin)

        if input_handler.is_dragging():
            renderer_instance.draw_mouse_highlight(mouse_pos)
            renderer_instance.draw_dragging_piece(dragging_piece, mouse_pos)


        pygame.display.flip()
        clock.tick(500)