import math
import pygame
import settings
from raycasting import optimized_raycasting, raycasting
from map import mini_map


class Drawing:
    """
    Classe responsável por desenhar todos os elementos na tela.
    """
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(
            self.screen,
            settings.SKYBLUE,
            (0, 0, settings.WIDTH, settings.HALF_HEIGHT)
        )
        pygame.draw.rect(
            self.screen,
            settings.DARKGRAY,
            (0, settings.HALF_HEIGHT,
            settings.WIDTH,
            settings.HALF_HEIGHT)
        )

    def world(self, player_position, player_angle):
        # raycasting(self.screen, player_position, player_angle)
        optimized_raycasting(self.screen, player_position, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, settings.RED)
        self.screen.blit(render, settings.FPS_POSITION)

    def mini_map(self, player):
        self.screen_map.fill(settings.BLACK)
        map_x = player.x // settings.MAP_SCALE
        map_y = player.y // settings.MAP_SCALE

        # Desenha a linha de direção do player
        pygame.draw.line(
            self.screen_map,
            settings.YELLOW,
            (map_x, map_y),
            (
                map_x + 12 * math.cos(player.angle),
                map_y + 12 * math. sin(player.angle)
            ),
            2
        )

        # Desenha o player
        pygame.draw.circle(
            self.screen_map,
            settings.RED,
            (int(map_x), int(map_y)),
            5
        )

        # Desenha o mini mapa
        for x, y in mini_map:
            pygame.draw.rect(
                self.screen_map,
                settings.GREEN,
                (x, y, settings.MAP_TILE, settings.MAP_TILE)
            )
        self.screen.blit(self.screen_map, settings.MAP_POSITION)
