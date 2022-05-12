import pygame
import sys
from pygame.locals import *


class MenuView:
    """Luokka, joka hallitseen aloitusvalikon näyttämisen
    """
    def __init__(self, display, font, width, height):
        """Luokan konstruktori, joka alustaa piirtämiseen tarvittavia muuttujia

        Args:
            display : pygame display objekti jolla näkymä piirretään
            font : pygame font objekti jolla kirjoitetaan peli-ikkunaan
            width (kokonaisluku): peli-ikkunan leveys
            height (kokonaisluku): peli-ikkunan korkeus
        """
        self.state = "menu"

        self._display = display
        self._font = font
        self._width = width
        self._height = height
        self._new_game_button = None
        self._view_highscores_button = None

    def draw_menu(self):
        """Piirtää aloitusvalikon
        """
        self._display.fill((255, 255, 255))
        new_game_text = self._font.render("New game", True, (255, 255, 255))
        new_game_button = new_game_text.get_rect(center=(self._width//2, self._height//2))
        self._new_game_button = new_game_button
        pygame.draw.rect(self._display, (0, 0, 0), new_game_button, border_radius=5)
        self._display.blit(new_game_text, new_game_button)

        view_highscores_text = self._font.render("View highscores", True, (255, 255, 255))
        view_highscores_button = view_highscores_text.get_rect(center=(self._width//2, self._height//2+new_game_button.height+new_game_button.height//2))
        self._view_highscores_button = view_highscores_button
        pygame.draw.rect(self._display, (0, 0, 0), view_highscores_button, border_radius=5)
        self._display.blit(view_highscores_text, view_highscores_button)

    def event_handler(self):
        """Hallitseen käyttäjän antamaa syötettä
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._new_game_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "game"
                if self._view_highscores_button.collidepoint(pygame.mouse.get_pos()):
                    self.state = "highscores"

    def set_state(self, state):
        """Asettaa näkymän uuden tilan

        Args:
            state (merkkijono): uusi tila
        """
        self.state = state

    def check_state(self):
        """Palauttaa näkymän tämänhetkisen tilan

        Returns:
            merkkijono: tila
        """
        return self.state