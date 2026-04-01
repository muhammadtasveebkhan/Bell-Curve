import pygame
import random

class DataPoint(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        # Randomly decide if it's "Good" point or an "Outlier"
        self.is_outlier = random() > 0.7 

        self.image = pygame.Surface((20, 20))
        