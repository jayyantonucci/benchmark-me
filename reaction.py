import pygame
from datetime import datetime
import time
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((420, 420))
game_font = pygame.freetype.SysFont()
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

