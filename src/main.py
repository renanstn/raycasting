import settings
from player import Player
from drawing import Drawing
from map import world_map
import math
import pygame


pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(settings.BLACK)
    drawing.background()
    drawing.world(player.position, player.angle)
    drawing.fps(clock)
    if settings.SHOW_MAP:
        drawing.map()
        drawing.player_in_map(player)

    pygame.display.flip()
    clock.tick(settings.FPS)
