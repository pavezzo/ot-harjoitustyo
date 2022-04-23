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
        self.view_highscores_button = None

    def draw_menu(self):
        self.display.fill((255, 255, 255))
        #new_game_button = pygame.draw.rect(self.display, (139, 0, 0), center=(self.width//2, self.height//2), 400, 200)
        #self.new_game_button = new_game_button
        #new_game_text = self.font.render("New game", True, (0, 0, 0))
        #self.display.blit(new_game_text, (self.width//2, self.height//2))
        new_game_text = self.font.render("New game", True, (255, 255, 255))
        new_game_button = new_game_text.get_rect(center=(self.width//2, self.height//2))
        self.new_game_button = new_game_button
        pygame.draw.rect(self.display, (0, 0, 0), new_game_button, border_radius=5)
        self.display.blit(new_game_text, new_game_button)

        view_highscores_text = self.font.render("View highscores", True, (255, 255, 255))
        view_highscores_button = view_highscores_text.get_rect(center=(self.width//2, self.height//2+new_game_button.height+new_game_button.height//2))
        self.view_highscores_button = view_highscores_button
        pygame.draw.rect(self.display, (0, 0, 0), view_highscores_button, border_radius=5)
        self.display.blit(view_highscores_text, view_highscores_button)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "game"
                if self.view_highscores_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "highscores"

    def set_state(self, state):
        self.state = state

    def check_state(self):
        return self.state