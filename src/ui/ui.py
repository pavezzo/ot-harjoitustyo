import pygame
import sys
from screeninfo import get_monitors
from pygame.locals import *
from ui.game_view import GameView
from ui.menu_view import MenuView
from ui.highscore_view import HighscoreView
from ui.save_score_view import SaveScoreView

class Ui:
    """Luokka, joka hallitsee ohjelman näkymän vaihtoa.

    Attributes:
        current_view: tämän hetkinen näkymä, voidaan asettaa jos halutaan 
    """
    def __init__(self):
        """Luokan konstruktori, jossa asetetaan erilaisia näkymien tarvitsemia arvoja ja kutsutaan ohjelman näkymien konstruktoreja.
        """
        pygame.init()
        self.current_view = "menu"

        self.width = None
        self.height = None
        self._set_window_size()

        self.display = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption("2048")
        self.font_size = self.width // 20
        self.font = pygame.font.SysFont(None, self.font_size)
        self.clock = pygame.time.Clock()

        self.menu_view = MenuView(self.display, self.font, self.width, self.height)
        self.game_view = GameView(self.display, self.font, self.width, self.height)
        self.save_score_view = SaveScoreView(self.display, self.width, self.height, self.font)
        self.highscore_view = HighscoreView(self.display, self.width, self.height, self.font)

    def main_loop(self):
        """Pelin pyörimisen hoitava silmukka, joka huolehtii näkymien muutoksesta.
        """
        while True:
            if self.current_view == "menu":
                self.menu_view.draw_menu()
                self.menu_view.event_handler()
                if self.menu_view.check_state() != "menu":
                    self.current_view = self.menu_view.check_state()
                    self.menu_view.set_state("menu")

            if self.current_view == "highscores":
                self.highscore_view.draw_highscore_view()
                self.highscore_view.event_handler()
                if self.highscore_view.check_state() != "highscores":
                    self.current_view = self.highscore_view.check_state()
                    self.highscore_view.set_state("highscores")

            if self.current_view == "game":
                self.game_view.event_handler()
                self.game_view.update_game()
                if self.game_view.check_state() != "game":
                    self.save_score_view.set_score(self.game_view.get_score())
                    self.current_view = self.game_view.check_state()
                    self.game_view.set_state("game")
                    self.game_view.restart_game()
            
            if self.current_view == "save_score":
                self.save_score_view.draw_view()
                self.save_score_view.event_handler()
                if self.save_score_view.check_state() != "save_score":
                    self.current_view = self.save_score_view.check_state()
                    self.save_score_view.set_state("save_score")

            
            pygame.display.update()
            self.clock.tick(30)

    def _set_window_size(self):
        """Funktio joka laskee screeninfo-kirjaston avulla sopivan koon ohjelman ikkunalle.
        """
        for m in get_monitors():
            if m.is_primary:
                if m.width > m.height:
                    self.width = m.height // 2
                    self.height = m.height // 2
                else:
                    self.width = m.width // 2
                    self.height = m.width //2
