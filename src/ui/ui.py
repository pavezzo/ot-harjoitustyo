import pygame
import sys
from pygame.locals import *
from ui.game_view import Game_view
from ui.menu_view import Menu_view


class Ui:
    def __init__(self, current_view="menu"):
        pygame.init()
        self.current_view = current_view
        self.width = 1000
        self.height = 1000
        self.game_display = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption("2048")
        self.font_size = self.width // 20
        self.font = pygame.font.SysFont(None, self.font_size)
        self.game_view = Game_view(self.game_display, self.font, self.width, self.height)
        self.clock = pygame.time.Clock()
        self.menu = Menu_view(self.game_display, self.font, self.width, self.height)


    def main_loop(self):
        while True:
            if self.current_view == "menu":
                self.menu.draw_menu()
                self.menu.event_handler()
                if self.menu.check_state() == "game":
                    self.current_view = "game"

            if self.current_view == "game":
                self.game_view.event_handler()
                self.game_view.update_game()
            
            pygame.display.update()
            self.clock.tick(30)


