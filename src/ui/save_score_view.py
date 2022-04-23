import pygame
import sys
from pygame.locals import *
from repositories.highscores_repository import HighscoresRepository

class SaveScoreView:
    def __init__(self, display, width, height, font):
        self.display = display
        self.width = width
        self.height = height
        self.font = font
        self.score = None
        self.username = ""
        self.highscore_repository = HighscoresRepository()
        self.save_button = None
        self.current_state = "save_score"

    def set_score(self, score):
        self.score = score

    def draw_view(self):
        self.display.fill((255, 255, 255))
        score_text = self.font.render("Your score: " + str(self.score), True, (255, 0, 0))
        score_rect = score_text.get_rect(center=(self.width//2, self.height//2))

        prompt_text = self.font.render("Enter username: ", True, (255, 0, 0))
        prompt_rect = prompt_text.get_rect(center=(self.width//2, self.height//2+score_rect.height))
        
        if self.username != "":
            username_text = self.font.render(self.username, True, (255, 0, 0))
            username_rect = username_text.get_rect(center=(self.width//2, prompt_rect.top+prompt_rect.height+prompt_rect.height//2))
            self.display.blit(username_text, username_rect)
        else:
            username_rect = pygame.Rect(prompt_rect.left, prompt_rect.top+prompt_rect.height, prompt_rect.width, prompt_rect.height)
            pygame.draw.rect(self.display, (255, 0, 0), username_rect)
        
        save_text = self.font.render("Save", True, (255, 0, 0))
        save_button = save_text.get_rect(center=(self.width//2, username_rect.top+username_rect.height+username_rect.height//2))
        self.save_button = save_button

        self.display.blit(score_text, score_rect)
        self.display.blit(prompt_text, prompt_rect)
        self.display.blit(save_text, save_button)

    def check_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                else:
                    self.username += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.save_button.collidepoint(pygame.mouse.get_pos()):
                    if self.username != "":
                        self.highscore_repository.new_score(self.score, self.username)
                        self.current_state = "menu"