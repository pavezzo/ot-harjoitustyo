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

    def update_game(self):
        if not self.game.can_continue():
            return self.game_over()

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

    def game_over(self):
        #self.game_display.fill((255, 255, 255))

        game_over_text = self.font.render("Game over", True, (139, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.width//2, self.height//2))
        self.game_display.blit(game_over_text, game_over_rect) 