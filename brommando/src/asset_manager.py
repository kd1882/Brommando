# src/assets_manager.py
import pygame
import os

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def load_image(self, name, path):
        if name not in self.images:
            image = pygame.image.load(os.path.join('assets/images', path))
            self.images[name] = image
        return self.images[name]

    def load_sound(self, name, path):
        if name not in self.sounds:
            sound = pygame.mixer.Sound(os.path.join('assets/sounds', path))
            self.sounds[name] = sound
        return self.sounds[name]

    def load_font(self, name, path, size):
        if (name, size) not in self.fonts:
            font = pygame.font.Font(os.path.join('assets/fonts', path), size)
            self.fonts[(name, size)] = font
        return self.fonts[(name, size)]

