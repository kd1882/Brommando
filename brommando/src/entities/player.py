import pygame

class Player:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x, y, 50, 50)  # Example player size

    def update(self, keys):
        # Keyboard movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        # Update the player's rect position
        self.rect.update(self.x, self.y, 50, 50)

    def draw(self, screen):
        # Draw the player to the screen
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    # Placeholder for mouse handling method
    def handle_mouse(self, mouse_position):
        # Implement mouse movement or aiming here
        pass