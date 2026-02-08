import pygame

from models.board import Board
from ui import renderer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

renderer_instance = renderer.Renderer(screen)
board = Board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    renderer_instance.draw_board()
    renderer_instance.draw_pieces(board)
    pygame.display.flip()