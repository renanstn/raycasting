import settings
from player import Player
import pygame


pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(settings.BLACK)

    pygame.draw.circle(screen, settings.GREEN, player.position, 12)

    pygame.display.flip()
    clock.tick(settings.FPS)
