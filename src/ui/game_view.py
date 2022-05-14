import pygame
import sys
from pygame.locals import *
from logic.game import Game

colors = {
    "None": pygame.colordict.THECOLORS['white'],
    "2": pygame.colordict.THECOLORS['maroon4'],
    "4": pygame.colordict.THECOLORS['tan1'],
    "8": pygame.colordict.THECOLORS['springgreen'],
    "16": pygame.colordict.THECOLORS['slateblue'],
    "32": pygame.colordict.THECOLORS['sienna'],
    "64": pygame.colordict.THECOLORS['seagreen'],
    "128": pygame.colordict.THECOLORS['royalblue4'],
    "256": pygame.colordict.THECOLORS['rosybrown1'],
    "512": pygame.colordict.THECOLORS['red'],
    "1024": pygame.colordict.THECOLORS['purple'],
    "2048": pygame.colordict.THECOLORS['plum4'],
    "4096": pygame.colordict.THECOLORS['peru'],
    "8192": pygame.colordict.THECOLORS['orangered']
}


class GameView:
    """Luokka, joka hallitsee pelinäkymää
    """
    def __init__(self, display, font, width, height):
        """Luokan konstruktori, jossa alustetaan pelin loogisesta puolesta vastaava luokka, sekä
        erilaisia mittoja joita pelin näyttämiseen tarvitaan

        Args:
            display : pygame display objekti, jolla piirretään peliä
            font : pygame font objekti, jolla hallitaan ruudulle kirjoittamista
            width (kokonaisluku): peli-ikkunan leveys
            height (kokonaisluku): peli-ikkunan korkeus
        """
        self.current_state = "game"

        self._game = Game()
        self._game_size = 4
        self._display = display
        self._font = font
        self._width = width
        self._height = height
        self._box_padding = None
        self._text_padding_width = None
        self._text_padding_height = None
        self._box_size = None
        self.set_game_size()
        self._game_over = False
        self._main_menu_button = None
        self._save_score_button = None
        self._restart_button = None

    def set_game_size(self, size=4):
        self._game_size = size
        self._game.new_game(size)
        self._box_padding = self._width // (self._game_size * 40)
        self._text_padding_width = self._width//(2*self._game_size) - self._box_padding
        self._text_padding_height = self._height//(2*self._game_size) - self._box_padding
        self._box_size = (self._width//self._game_size - (2*self._box_padding), self._height//self._game_size - (2*self._box_padding))

    def event_handler(self):
        """Hallinoi käyttäjän syötettä ja välittää sen pelistä huolehtivalle luokalle
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._game.new_keypress("up")
                if event.key == pygame.K_DOWN:
                    self._game.new_keypress("down")
                if event.key == pygame.K_RIGHT:
                    self._game.new_keypress("right")
                if event.key == pygame.K_LEFT:
                    self._game.new_keypress("left")
                if event.key == pygame.K_SPACE:
                    self._game.restart_game()
                    self._game_over = False
            if event.type == pygame.MOUSEBUTTONDOWN and self._game_over:
                if self._main_menu_button.collidepoint(pygame.mouse.get_pos()):
                    self.current_state = "menu"
                if self._save_score_button.collidepoint(pygame.mouse.get_pos()):
                    self.current_state = "save_score"
                if self._restart_button.collidepoint(pygame.mouse.get_pos()):
                    self._game.restart_game()
                    self._game_over = False

    def update_game(self):
        """Huolehtii pelin graafisesta päivittämisestä game-luokan perusteella
        """
        if self._game_over:
            return self.game_over_view()

        self._display.fill((0, 0, 0))
        state = self._game.get_gamestate()

        for i in range(len(state)):
            for j in range(len(state[i])):
                pygame.draw.rect(self._display, colors[str(state[i][j])], ((self._box_padding+j*(self._width//self._game_size), self._box_padding+i*(self._height//self._game_size)), self._box_size))
                if state[i][j] is not None:
                    text = self._font.render(str(state[i][j]), True, (0, 0, 0))
                    self._display.blit(text, (self._text_padding_width+j*self._width//self._game_size, self._text_padding_height+i*self._height//self._game_size))

        score = self._game.get_score()
        score_text = self._font.render("Score: " + str(score), True, (0, 0, 0))
        self._display.blit(score_text, (self._box_padding, self._box_padding))

        if not self._game.can_continue():
            self._game_over = True
            return self.game_over_view()

    def game_over_view(self):
        """Huolehtii pelin loppuessa ruudukon päälle piirrettävästä loppuvalikosta
        """
        game_over_text = self._font.render("Game over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self._width//2, self._height//2.5))

        main_menu_text = self._font.render("Main menu", True, (255, 0 , 0))
        main_menu_button = main_menu_text.get_rect(center=(self._width//2, game_over_rect.top + 1.6*game_over_rect.height))
        pygame.draw.rect(self._display, (0, 0, 0), main_menu_button)        
        self._main_menu_button = main_menu_button

        restart_game_text = self._font.render("Restart game", True, (255, 0, 0))
        restart_game_button = restart_game_text.get_rect(center=(self._width//2, main_menu_button.top + 1.6*main_menu_button.height))
        self._restart_button = restart_game_button
        pygame.draw.rect(self._display, (0, 0, 0), restart_game_button)

        save_score_text = self._font.render("Save score", True, (255, 0, 0))
        save_score_button = save_score_text.get_rect(center=(self._width//2, restart_game_button.top + 1.6*restart_game_button.height))
        self._save_score_button = save_score_button
        pygame.draw.rect(self._display, (0, 0, 0), save_score_button)
       
        self._display.blit(game_over_text, game_over_rect)
        self._display.blit(main_menu_text, main_menu_button)
        self._display.blit(restart_game_text, restart_game_button) 
        self._display.blit(save_score_text, save_score_button)

    def check_state(self):
        """Palauttaa pelin tämänhetkisen tilan, käytäteen jos halutaan siirtyä näkymästä pois

        Returns:
            tämänhetkinen tila
        """
        return self.current_state

    def set_state(self, state):
        """Asettaa näkymän uuden tilan

        Args:
            state (merkkijono): uusi tila
        """
        self.current_state = state

    def get_score(self):
        """Palauttaa pelin tämänhetkisen pistemäärän

        Returns:
            kokonaisluku: pistemäärä
        """
        return self._game.get_score()

    def restart_game(self):
        """Aloittaa pelin alusta
        """
        self._game.restart_game()
        self._game_over = False