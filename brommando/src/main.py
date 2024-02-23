# src/main.py
import pygame
import settings

class Game:
    def __init__(self):  # Corrected method name
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def game_loop(self):
        while self.running:
            self.clock.tick(settings.FPS)  # Use self.clock

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def run(self):  # Implement the missing run method
        self.game_loop()

if __name__ == '__main__':
    game = Game()
    game.run()



# from assets_manager import AssetManager

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     clock = pygame.time.Clock()
#     running = True
#     #assets = AssetManager()

#     # Example of loading assets
#     #player_image = assets.load_image('player', 'player.png')
#     #background_music = assets.load_sound('background', 'music.ogg')
#     #game_font = assets.load_font('default', 'OpenSans-Bold.ttf', 24)

#     # Play background music
#     #background_music.play(-1)  # Loop indefinitely

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         #screen.fill((0, 0, 0))  # Clear screen

#         # Game logic and rendering
#         #screen.blit(player_image, (100, 100))  # Example of using an asset

#         #pygame.display.flip()  # Update the display
#         clock.tick(60)  # Maintain 60 FPS

#     pygame.quit()


