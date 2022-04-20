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
    
    def update_game(self):
        self.game_display.fill((0, 0, 0))
        state = self.game.get_gamestate()

        for i in range(len(state)):
            for j in range(len(state[i])):
                pygame.draw.rect(self.game_display, (255, 255, 255), (10+j*(self.width//4), 10+i*(self.height//4), self.width//4-25, self.height//4-25))
                if state[i][j] is not None:
                    text = self.font.render(str(state[i][j]), True, (0, 0, 0))
                    self.game_display.blit(text, (250+j*self.width//4, 250+i*self.height//4))

        score = self.game.get_score()
        score_text = self.font.render("Score: " + str(score), True, (0, 0, 0))
        self.game_display.blit(score_text, (0, 0))


    