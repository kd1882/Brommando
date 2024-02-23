# src/main.py
import pygame
import settings
# from assets_manager import AssetManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def game_loop(self):
        while self.running:
            self.clock.tick(settings.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def run(self): 
        self.game_loop()

if __name__ == '__main__':
    game = Game()
    game.run()