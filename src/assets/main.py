"""
Bell Curve Catcher - Main Entry Point
Author: Muhammad Khan
Date: April 2026
Description: This script handles the Pygame initialization, the main game loop,
and collision logic for the Bell Curve Catcher project.
"""
import pygame
import os 
import random
from sprites import DataPoint, Catcher

# # Path Logic for Assets
GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename:str) -> str:
    return os.path.join(GAME_PATH,"assets", filename)

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bell Curve Catcher")
clock = pygame.time.Clock()


#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def main():
    """Sets up game groups, timers, and handles the primary game loop."""
    running = True
    score = 0
    font = pygame.font.SysFont("Arial", 36)

    # Groups
    points_group = pygame.sprite.Group()
    player = Catcher(WIDTH, HEIGHT)
    player_group = pygame.sprite.GroupSingle(player)

    # Timer: Spawn every 800ms (slightly faster)
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 800)

    while running:
        screen.fill(WHITE)

        # 1. Draw the "Bell Curve" Center (Safe Zone)
        # 440 to 840 is the middle 400 pixels of a 1280 screen
        pygame.draw.rect(screen, GRAY, (440, 0, 400, HEIGHT))

        for event in pygame.event.get():
            # Standard quit event (clicking the close button)
            if event.type == pygame.QUIT:
                running = False
            
            # Keydown events (detecting when a key is pressed once)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            # Timer event for spawning points
            if event.type == SPAWN_EVENT:
                new_point = DataPoint(WIDTH)
                points_group.add(new_point)

        # 2. Update
        points_group.update()
        player_group.update()

        # 3. Collision Logic
        hits = pygame.sprite.spritecollide(player, points_group, True)
        for hit in hits:
            if not hit.is_outlier:
                score += 10
            else:
                score -= 20 # Outliers hurt more!

        # 4. Draw Everything
        points_group.draw(screen)
        player_group.draw(screen)
        
        # Display Score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

