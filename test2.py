import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))

player = pygame.image.load('player2.1.png').convert()
wall = pygame.image.load('bush2.1.png').convert()
floor = pygame.image.load('grass2.1.png').convert()

background = [[wall]*20,
              [floor]*20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [floor] * 20,
              [wall]*20]


for x in range(0, 20):
    for y in range(0, 20):
        screen.blit(background[x][y], (x * 40, y * 40))

position = player.get_rect()
position = position.move(40, 40)
posxy = [1, 1]

screen.blit(player, position)

pygame.display.update()

while True:
    screen.blit(background[posxy[0]][posxy[1]], (posxy[0]*40, posxy[1]*40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                position = position.move(0, -40)
                posxy[1] -= 1
            elif event.key == pygame.K_a:
                position = position.move(-40, 0)
                posxy[0] -= 1
            elif event.key == pygame.K_s:
                position = position.move(0, 40)
                posxy[1] += 1
            elif event.key == pygame.K_d:
                position = position.move(40, 0)
                posxy[0] += 1
    screen.blit(player, position)
    pygame.display.update()
