# src/main.py
import pygame
from assets_manager import AssetManager
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    assets = AssetManager()

    # Example of loading assets
    player_image = assets.load_image('player', 'player.png')
    background_music = assets.load_sound('background', 'music.ogg')
    game_font = assets.load_font('default', 'OpenSans-Bold.ttf', 24)

    # Play background music
    background_music.play(-1)  # Loop indefinitely

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear screen

        # Game logic and rendering
        screen.blit(player_image, (100, 100))  # Example of using an asset

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()

if __name__ == '__main__':
    main()

