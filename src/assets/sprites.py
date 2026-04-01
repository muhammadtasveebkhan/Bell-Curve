import pygame
import random

class DataPoint(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        # Randomly decide if it's "Good" point or an "Outlier"
        self.is_outlier = random() > 0.7 

        self.image = pygame.Surface((20, 20))
        if self.is_outlier:
            self.image.fill((255, 0, 0)) # Red for outliers
        else:
            self.image.fill((0, 255, 0)) # Green for valid data

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 20)
        self.rect.y = -20
        self.speed = random.ranint(2, 5)
    
    def update(self):
        self.rect.y += self.speed
                    