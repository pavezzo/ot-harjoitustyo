import pygame
import sys
from pygame.locals import *


class Menu_view:
    def __init__(self, display, font, width, height):
        self.display = display
        self.font = font
        self.state = "menu"
        self.width = width
        self.height = height
        self.new_game_button = None

    def draw_menu(self):
        self.display.fill((255, 255, 255))
        new_game_button = pygame.draw.rect(self.display, (255, 255, 255), (self.width//2, self.height//2, 200, 100))
        self.new_game_button = new_game_button
        new_game_text = self.font.render("New game", True, (0, 0, 0))
        self.display.blit(new_game_text, (self.width//2, self.height//2))

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "game"


    def check_state(self):
        return self.state