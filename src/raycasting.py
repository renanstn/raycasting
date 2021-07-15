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
            # pygame.draw.line(
            #     screen,
            #     settings.DARKGRAY,
            #     player_position,
            #     (x, y),
            #     2
            # )
            if (x // settings.TILE * settings.TILE, y // settings.TILE * settings.TILE) in world_map:
                # Corrige efeito de "olho de peixe"
                depth *= math.cos(player_angle - cur_angle)
                # Calcula a altura de cada linha de projeção
                projection_height = settings.PROJECTION_COEFFICIENT / depth
                # Calcula a cor da parede de acordo com a "distância" da mesma
                rgb_color = 255 / (1 + depth * depth * 0.0001)
                # color = (rgb_color, rgb_color, rgb_color)
                color = (rgb_color // 2, rgb_color, rgb_color // 3)
                # Desenha o mundo 3D, toda a magia acontece bem aqui:
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        ray * settings.SCALE,
                        settings.HALF_HEIGHT - projection_height // 2,
                        settings.SCALE,
                        projection_height
                    )
                )
                break
        cur_angle += settings.DELTA_ANGLE
