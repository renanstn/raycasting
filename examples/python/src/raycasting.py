import settings
from map import world_map
import pygame
import math


def raycasting(screen, player_position: tuple, player_angle: int):
    current_angle = player_angle - settings.HALF_FOV
    xo, yo = player_position
    for ray in range(settings.NUM_RAYS):
        sin_a = math.sin(current_angle)
        cos_a = math.cos(current_angle)
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
                depth *= math.cos(player_angle - current_angle)
                # Calcula a altura de cada linha de projeção
                projection_height = settings.PROJECTION_COEFFICIENT / depth
                # Calcula a cor da parede de acordo com a "distância" da mesma
                rgb_color = 255 / (1 + depth * depth * 0.00002)
                # color = (rgb_color, rgb_color, rgb_color)
                color = (rgb_color, rgb_color  // 2, rgb_color // 3)
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
        current_angle += settings.DELTA_ANGLE


def mapping(a, b):
    return (
        (a // settings.TILE) * settings.TILE,
        (b // settings.TILE) * settings.TILE
    )


def optimized_raycasting(
    screen,
    player_position: tuple,
    player_angle: int,
    textures: tuple
):
    ox, oy = player_position
    xm, ym = mapping(ox, oy)
    current_angle = player_angle - settings.HALF_FOV
    for ray in range(settings.NUM_RAYS):
        sin_a = math.sin(current_angle)
        cos_a = math.cos(current_angle)

        # Cálculo vertical
        x, dx = (xm + settings.TILE, 1) if cos_a >= 0 else (xm, -1)
        for _ in range(0, settings.WIDTH, settings.TILE):
            depth_vertical = (x - ox) / cos_a
            yv = oy + depth_vertical * sin_a
            tile_vertical = mapping(x + dx, yv)
            if tile_vertical in world_map:
                texture_vertical = world_map[tile_vertical]
                break
            x += dx * settings.TILE

        # Cálculo horizontal
        y, dy = (ym + settings.TILE, 1) if sin_a >= 0 else (ym, -1)
        for _ in range(0, settings.WIDTH, settings.TILE):
            depth_horizontal = (y - oy) / sin_a
            xh = ox + depth_horizontal * cos_a
            tile_horizontal = mapping(xh, y + dy)
            if tile_horizontal in world_map:
                texture_horizontal = world_map[tile_horizontal]
                break
            y += dy * settings.TILE

        # Projeção
        # depth = min(depth_horizontal, depth_vertical)
        if depth_vertical < depth_horizontal:
            depth, offset, texture = (depth_vertical, yv, texture_vertical)
        else:
            depth, offset, texture = (depth_horizontal, xh, texture_horizontal)

        offset = int(offset) % settings.TILE
        # Corrige efeito de "olho de peixe"
        depth *= math.cos(player_angle - current_angle)
        depth = max(depth, 0.00001)
        # Calcula a altura de cada linha de projeção
        projection_height = min(
            int(settings.PROJECTION_COEFFICIENT / depth),
            2 * settings.HEIGHT
        )

        if settings.TEXTURES_ON:
            # Calcula o offset da textura
            wall_column = textures[texture].subsurface(
                offset * settings.TEXTURE_SCALE,
                0,
                settings.TEXTURE_SCALE,
                settings.TEXTURE_HEIGHT
            )
            wall_column = pygame.transform.scale(
                wall_column,
                (settings.SCALE, projection_height)
            )
            # Desenha a textura
            screen.blit(
                wall_column,
                (
                    ray * settings.SCALE,
                    settings.HALF_HEIGHT - projection_height // 2
                )
            )
        else:
            # Calcula a cor da parede de acordo com a "distância" da mesma
            rgb_color = 255 / (1 + depth * depth * 0.00002)
            # color = (rgb_color, rgb_color, rgb_color)
            color = (rgb_color, rgb_color  // 2, rgb_color // 3)
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

        current_angle += settings.DELTA_ANGLE
