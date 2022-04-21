import pygame
from pygame.locals import *
from repositories.highscores_repository import HighscoresRepository

class HighscoreView:
    def __init__(self, display, width, height, font):
        self.display = display
        self.width = width
        self.height = height
        self.font = font
        self.highscores = HighscoresRepository()

    def draw_highscore_view(self):
        highscores = self.highscores.get_top_10()