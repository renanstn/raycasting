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
        self.textures = {
            '1': pygame.image.load('textures/wall1.png').convert(),
            '2': pygame.image.load('textures/wall2.png').convert(),
            'S': pygame.image.load('textures/sky3.png').convert(),
        }

    def background(self, angle):
        # Desenha o céu
        if settings.TEXTURES_ON:
            # Calcula o offset da movimentação do céu quando o player gira
            sky_offset = -10 * math.degrees(angle) % settings.WIDTH
            self.screen.blit(self.textures['S'], (sky_offset, 0))
            self.screen.blit(self.textures['S'], (sky_offset - settings.WIDTH, 0))
            self.screen.blit(self.textures['S'], (sky_offset + settings.WIDTH, 0))
        else:
            pygame.draw.rect(
                self.screen,
                settings.SKYBLUE,
                (0, 0, settings.WIDTH, settings.HALF_HEIGHT)
            )
        # Desenha o chão
        pygame.draw.rect(
            self.screen,
            settings.DARKGRAY,
            (0, settings.HALF_HEIGHT,
            settings.WIDTH,
            settings.HALF_HEIGHT)
        )

    def world(self, player_position, player_angle):
        # raycasting(self.screen, player_position, player_angle)
        optimized_raycasting(
            self.screen,
            player_position,
            player_angle,
            self.textures
        )

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, settings.DARKORANGE)
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
                map_y + 12 * math.sin(player.angle)
            ),
            2
        )

        # Desenha a posição do player
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
                settings.DARKBROWN,
                (x, y, settings.MAP_TILE, settings.MAP_TILE)
            )
        self.screen.blit(self.screen_map, settings.MAP_POSITION)
