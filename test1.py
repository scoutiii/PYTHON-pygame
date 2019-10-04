import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((1152, 648))

print("pygame initialized")

player = pygame.image.load('player1.bmp').convert()
background = pygame.image.load('background1.bmp').convert()

screen.blit(background, (0, 0))

position = player.get_rect()
position = position.move(0, 400)

screen.blit(player, position)

pygame.display.update()
pygame.key.set_repeat(50, 10)

while True:
    screen.blit(background, position, position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                position = position.move(0, -1)
            if event.key == pygame.K_s:
                position = position.move(0, 1)
            if event.key == pygame.K_a:
                position = position.move(-1, 0)
            if event.key == pygame.K_d:
                position = position.move(1, 0)

    screen.blit(player, position)
    pygame.display.update()
    pygame.time.delay(10)
