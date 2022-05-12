import pygame
import sys
from pygame.locals import *
from repositories.highscores_repository import HighscoresRepository

class SaveScoreView:
    """Luokka, joka hallitsee tuloksen tallentamiseen käytettävää näkymää
    """
    def __init__(self, display, width, height, font):
        """Luokan konstruktori, joka alustaa näkymään tarvittavia muuttujia

        Args:
            display : pygame display objekti, jolla piirretään näkymä
            width (kokonaisluku): peli-ikkunan leveys
            height (kokonaisluku): peli-ikkunan korkeus
            font : pygame font objekti, jolla hallitaan ruudulle kirjoittamista
        """
        self.score = None
        self.username = ""
        self.current_state = "save_score"

        self._display = display
        self._width = width
        self._height = height
        self._font = font
        self._highscore_repository = HighscoresRepository()
        self._save_button = None

    def set_score(self, score):
        """Asettaa käyttäjän pelituksen näkymään

        Args:
            score (kokonaisluku): käyttäjän saama pistetulos pelistä
        """
        self.score = score

    def draw_view(self):
        """Piirtää näkymän ja päivittää siihen käyttäjän kirjoittaman käyttäjänimen
        """
        self._display.fill((255, 255, 255))
        score_text = self._font.render("Your score: " + str(self.score), True, (255, 0, 0))
        score_rect = score_text.get_rect(center=(self._width//2, self._height//2))

        prompt_text = self._font.render("Enter username: ", True, (255, 0, 0))
        prompt_rect = prompt_text.get_rect(center=(self._width//2, self._height//2+score_rect.height))
        
        if self.username != "":
            username_text = self._font.render(self.username, True, (255, 0, 0))
            username_rect = username_text.get_rect(center=(self._width//2, prompt_rect.top+prompt_rect.height+prompt_rect.height//2))
            self._display.blit(username_text, username_rect)
        else:
            username_rect = pygame.Rect(prompt_rect.left, prompt_rect.top+prompt_rect.height, prompt_rect.width, prompt_rect.height)
            pygame.draw.rect(self._display, (255, 0, 0), username_rect)
        
        save_text = self._font.render("Save", True, (255, 0, 0))
        save_button = save_text.get_rect(center=(self._width//2, username_rect.top+username_rect.height+username_rect.height//2))
        self._save_button = save_button

        self._display.blit(score_text, score_rect)
        self._display.blit(prompt_text, prompt_rect)
        self._display.blit(save_text, save_button)

    def check_state(self):
        """Palauttaa näkymän tämänhetkisen tilan

        Returns:
            merkkijono: tämänhetkinen tila
        """
        return self.current_state

    def set_state(self, state):
        """Asettaa näkymälle uuden tilan

        Args:
            state (merkkijono): uusi tila
        """
        self.current_state = state

    def event_handler(self):
        """Hallitsee käyttäjän antamia syötteitä
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                elif event.key == pygame.K_RETURN:
                    if self.username != "":
                        self._highscore_repository.new_score(self.score, self.username)
                        self.current_state = "menu"
                        self.usernmae = ""
                else:
                    self.username += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._save_button.collidepoint(pygame.mouse.get_pos()):
                    if self.username != "":
                        self._highscore_repository.new_score(self.score, self.username)
                        self.current_state = "menu"
                        self.username = ""