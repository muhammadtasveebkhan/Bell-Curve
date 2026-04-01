import pygame
import os 
import random
from sprites import DataPoint

# Project Path Logic 
GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename:str) -> str:
    return os.path.join(GAME_PATH,"assets", filename)

#Initializing Pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Bell Curve Catcher")
clock = pygame.time.Clock()

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def main():
    running = True
    score = 0
    points = pygame.sprite.Group()

    #Timer for spawning points
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1000)

    while running:
        screen.fill(WHITE)

        # 1. Draw the "Safe Zone" (The Bell Curve Area)
        # 2. For now, let's represent the "Safe" center of the curve
        pygame.draw