import settings
import raycasting
from player import Player
from map import world_map
import math
import pygame


pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Computa os movimentos do player
    player.movement()
    # Preenche o background
    screen.fill(settings.BLACK)

    # Calcula o raycasting
    raycasting.raycasting(screen, player.position, player.angle)

    # Desenha o player
    pygame.draw.circle(
        screen,
        settings.GREEN,
        (int(player.x), int(player.y)),
        12
    )

    # Desenha a linha de direção do player
    pygame.draw.line(
        screen,
        settings.GREEN,
        player.position,
        (
            player.x + settings.WIDTH * math.cos(player.angle),
            player.y + settings.WIDTH * math. sin(player.angle)
        ),
        2
    )

    # Desenha o mapa
    for x, y in world_map:
        pygame.draw.rect(
            screen,
            settings.DARKGRAY,
            (x, y, settings.TILE, settings.TILE),
            2
        )

    pygame.display.flip()
    clock.tick(settings.FPS)
