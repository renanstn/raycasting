import math
import pygame
import settings
from raycasting import optimized_raycasting, raycasting
from map import world_map


class Drawing:
    """
    Classe responsável por desenhar todos os elementos na tela.
    """
    def __init__(self, screen):
        self.screen = screen
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

    def map(self):
        for x, y in world_map:
            pygame.draw.rect(
                self.screen,
                settings.DARKGRAY,
                (x, y, settings.TILE, settings.TILE),
                2
            )

    def player_in_map(self, player):
        # Desenha o player
        pygame.draw.circle(
            self.screen,
            settings.GREEN,
            (int(player.x), int(player.y)),
            12
        )
        # Desenha a linha de direção do player
        pygame.draw.line(
            self.screen,
            settings.GREEN,
            player.position,
            (
                player.x + settings.WIDTH * math.cos(player.angle),
                player.y + settings.WIDTH * math. sin(player.angle)
            ),
            2
        )
