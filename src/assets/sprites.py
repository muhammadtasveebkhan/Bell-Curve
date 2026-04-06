import pygame
import random

class DataPoint(pygame.sprite.Sprite):
    '''Represents the falling data points (Green = Good, Red = Outlier).'''
    def __init__(self, screen_width):
        super().__init__()
        # Logic: 30% chance to