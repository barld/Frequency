import pygame
from Board.Units.Unit import Unit


class Soldier(Unit):
    def __init__(self, player, tile):
        self.Texture = pygame.transform.scale(pygame.image.load('images/units/soldierGreen.png'), [35, 35])
        super().__init__(player, tile, self.Texture)