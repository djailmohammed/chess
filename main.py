import pygame

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

        elif event.type == pygame.MOUSEMOTION:
                input_handler.handle_mouse_motion(event.pos)

    screen.fill((0, 0, 0))

    renderer_instance.draw_board()
    dragging_piece, mouse_pos, drag_origin = input_handler.get_dragging_info()
    selected_piece, selected_origin = input_handler.get_selected_info()

    if input_handler.is_selected() and not input_handler.is_dragging():
        renderer_instance.draw_highlight(selected_origin)
        renderer_instance.draw_legal_moves(selected_piece.get_valid_moves(board.grid))

    renderer_instance.draw_pieces(board, dragging_piece)

    if input_handler.is_dragging():
        renderer_instance.draw_mouse_highlight(mouse_pos)
        renderer_instance.draw_highlight(selected_origin)
        renderer_instance.draw_legal_moves(selected_piece.get_valid_moves(board.grid))
        renderer_instance.draw_dragging_piece(dragging_piece, mouse_pos)


    pygame.display.flip()
    clock.tick(120)