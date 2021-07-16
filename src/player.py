import settings
import math
import pygame


class Player:
    """
    Classe que representa o jogador e suas possíveis ações.
    """
    def __init__(self) -> None:
        self.x, self.y = settings.player_position
        self.angle = settings.player_angle

    @property
    def position(self) -> tuple:
        return (self.x, self.y)

    def movement(self) -> None:
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += settings.player_speed * cos_a
            self.y += settings.player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -settings.player_speed * cos_a
            self.y += -settings.player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += settings.player_speed * sin_a
            self.y += -settings.player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -settings.player_speed * sin_a
            self.y += settings.player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
