import settings
from map import world_map
import pygame
import math


def raycasting(screen, player_position: tuple, player_angle: int):
    cur_angle = player_angle - settings.HALF_FOV
    xo, yo = player_position
    for ray in range(settings.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(settings.MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pygame.draw.line(
                screen,
                settings.DARKGRAY,
                player_position,
                (x, y),
                2
            )
            if (x // settings.TILE * settings.TILE, y // settings.TILE * settings.TILE) in world_map:
                break
        cur_angle += settings.DELTA_ANGLE
