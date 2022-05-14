import pygame
import sys
from pygame.locals import *
from repositories.highscores_repository import HighscoresRepository

class HighscoreView:
    """Luokka, joka hallitsee huipputulosten näyttämisen
    """
    def __init__(self, display, width, height, font):
        """Luokan konstruktori, joka alustaa näyttämiseen tarvittavia muuttujia

        Args:
            display : pygame display objekti, jolla piirretään ruudulle
            width (kokonaisluku): peli-ikkunan leveys
            height (kokonaisluku): peli-ikkunan korkeus
            font : pygame font objekti, jolla hallitaan ruudulle kirjoittamista
        """
        self.state = "highscores"

        self._display = display
        self._width = width
        self._height = height
        self._font = font
        self._highscores_repository = HighscoresRepository()
        self._back_to_menu_button = None

    def draw_highscore_view(self):
        """Hallitsee huipputulosten piirtämisen peli-ikkunaan
        """
        self._display.fill((255, 255, 255))
        highscores = self._highscores_repository.get_top_10()
        for i, row in enumerate(highscores):
            text = self._font.render(str(row[2]) + "x" + str(row[2]) + " grid: " + row[0] + " " + str(row[1]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self._width//2, self._height//10+i*self._height//20))
            self._display.blit(text, text_rect)

        back_to_menu_text = self._font.render("Back to menu", True, (255, 255, 255))
        back_to_menu_button = back_to_menu_text.get_rect()
        back_to_menu_button.left = 0
        back_to_menu_button.top = 0
        self._back_to_menu_button = back_to_menu_button
        pygame.draw.rect(self._display, (0, 0, 0), back_to_menu_button, border_radius=5)
        self._display.blit(back_to_menu_text, back_to_menu_button)

    def event_handler(self):
        """Hallitseen käyttäjän antamat syötteet
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._back_to_menu_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "menu"

    def set_state(self, state):
        """Asettaa näkymän uuden tilan

        Args:
            state (merkkijono): uusi tila
        """
        self.state = state

    def check_state(self):
        """Palauttaa näkymän tämänhetkisen tilan

        Returns:
            merkkijono: tämänhetkinen tila
        """
        return self.state
            