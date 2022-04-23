import pygame
import sys
from pygame.locals import *
from repositories.highscores_repository import HighscoresRepository

class HighscoreView:
    def __init__(self, display, width, height, font):
        self.display = display
        self.width = width
        self.height = height
        self.font = font
        self.highscores_repository = HighscoresRepository()

    def draw_highscore_view(self):
        self.display.fill((255, 255, 255))
        highscores = self.highscores_repository.get_top_10()
        for i, row in enumerate(highscores):
            text = self.font.render(row[0] + " " + str(row[1]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.width//2, self.height//10+i*self.height//20))
            self.display.blit(text, text_rect)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            