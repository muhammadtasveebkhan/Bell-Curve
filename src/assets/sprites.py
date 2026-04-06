import pygame
import random

class DataPoint(pygame.sprite.Sprite):
    '''Represents the falling data points (Green = Good, Red = Outlier).'''
    def __init__(self, screen_width):
        super().__init__()
        # Logic: 30% chance to be an outlier 
        self.is_outlier = random.random() > 0.7 

        self.image = pygame.Surface((20, 20))
        if self.is_outlier:
            self.image.fill((255, 0, 0)) # Red
        else:
            self.image.fill((0, 255, 0)) # Green

        self.rect = self.image.get_rect()
        