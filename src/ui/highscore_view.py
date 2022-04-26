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
        self.back_to_menu_button = None
        self.state = "highscores"

    def draw_highscore_view(self):
        self.display.fill((255, 255, 255))
        highscores = self.highscores_repository.get_top_10()
        for i, row in enumerate(highscores):
            text = self.font.render(row[0] + " " + str(row[1]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.width//2, self.height//10+i*self.height//20))
            self.display.blit(text, text_rect)

        back_to_menu_text = self.font.render("Back to menu", True, (0, 0, 0))
        back_to_menu_button = back_to_menu_text.get_rect()
        back_to_menu_button.left = self.width//20
        back_to_menu_button.top = 0
        self.back_to_menu_button = back_to_menu_button
        self.display.blit(back_to_menu_text, back_to_menu_button)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_to_menu_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "menu"

    def set_state(self, state):
        self.state = state

    def check_state(self):
        return self.state
            