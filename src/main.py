import settings
from player import Player
from drawing import Drawing
import pygame


pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
screen_map = pygame.Surface((
    settings.WIDTH // settings.MAP_SCALE,
    settings.HEIGHT // settings.MAP_SCALE
))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, screen_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(settings.BLACK)
    drawing.background(player.angle)
    drawing.world(player.position, player.angle)
    drawing.fps(clock)

    if settings.SHOW_MAP:
        drawing.mini_map(player)

    pygame.display.flip()
    clock.tick(settings.FPS)
