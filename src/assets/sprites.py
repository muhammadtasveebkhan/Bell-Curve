import pygame
import random

class DataPoint(pygame.sprite.Sprite):
    '''Represents the falling data points (Green = Good, Red = Outlier).'''
    def __init__(self, screen_width):
        """Initializes a data point with a random position and outlier status."""
        super().__init__()
        # Logic: 30% chance to be an outlier 
        self.is_outlier = random.random() > 0.7 

        self.image = pygame.Surface((20, 20))
        if self.is_outlier:
            self.image.fill((255, 0, 0)) # Red
        else:
            self.image.fill((0, 255, 0)) # Green

        self.rect = self.image.get_rect()
        # Spawn at a random X position at the top
        self.rect.x = random.randint(0, screen_width - 20)
        self.rect.y = -20
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 720: # Match the screen height
            self.kill()

class Catcher(pygame.sprite.Sprite):
    '''The player-controlled bucket to catch data points.'''
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((100, 40))
        self.image.fill((0, 0, 255)) # Blue Bucket
        self.rect = self.image.get_rect()
        
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 20
        self.speed = 12
        self.screen_width = screen_width
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Keep bucket on screen
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > self.screen_width: self.rect.right = self.screen_width