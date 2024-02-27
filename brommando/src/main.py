# src/main.py
import pygame
import settings
from entities.player import Player
# from assets_manager import AssetManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.player = Player(400, 300)
        self.running = True
        self.clock = pygame.time.Clock()


    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(settings.FPS)


    def run(self): 
        self.game_loop()

if __name__ == '__main__':
    game = Game()
    game.run()