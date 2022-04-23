import pygame
import sys
from pygame.locals import *
from logic.game import Game


class Game_view:
    def __init__(self, display, font, width, height):
        self.game = Game()
        self.game_display = display
        self.font = font
        self.width = width
        self.height = height
        self.text_padding_width = self.width//8 - 15
        self.text_padding_height = self.height//8 - 15
        self.game_over = False
        self.save_score_button = None
        self.current_state = "game"

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.new_keypress("up")
                if event.key == pygame.K_DOWN:
                    self.game.new_keypress("down")
                if event.key == pygame.K_RIGHT:
                    self.game.new_keypress("right")
                if event.key == pygame.K_LEFT:
                    self.game.new_keypress("left")
                if event.key == pygame.K_SPACE:
                    self.game.restart_game()
                    self.game_over = False
            if event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                if self.save_score_button.collidepoint(pygame.mouse.get_pos()):
                    self.current_state = "save_score"

    def update_game(self):
        if self.game_over:
            return self.game_over_view()

        self.game_display.fill((0, 0, 0))
        state = self.game.get_gamestate()

        for i in range(len(state)):
            for j in range(len(state[i])):
                pygame.draw.rect(self.game_display, (255, 255, 255), (10+j*(self.width//4), 10+i*(self.height//4), self.width//4-25, self.height//4-25))
                if state[i][j] is not None:
                    text = self.font.render(str(state[i][j]), True, (0, 0, 0))
                    self.game_display.blit(text, (self.text_padding_width+j*self.width//4, self.text_padding_height+i*self.height//4))

        score = self.game.get_score()
        score_text = self.font.render("Score: " + str(score), True, (0, 0, 0))
        self.game_display.blit(score_text, (0, 0))

        if not self.game.can_continue():
            self.game_over = True
            return self.game_over_view()

    def game_over_view(self):
        game_over_text = self.font.render("Game over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.width//2, self.height//2))
        save_score_text = self.font.render("Save score", True, (255, 0, 0))
        save_score_button = save_score_text.get_rect(center=(self.width//2, self.height//2+game_over_rect.height))
        self.save_score_button = save_score_button
        self.game_display.blit(game_over_text, game_over_rect) 
        self.game_display.blit(save_score_text, save_score_button)

    def check_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state

    def get_score(self):
        return self.game.get_score()

    def restart_game(self):
        self.game.restart_game()
        self.game_over = False