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


#         # 1. Draw the "Safe Zone" (The Bell Curve Area)
#         # For now, let's represent the "Safe" center of the curve
#         pygame.draw.rect(screen, GRAY, (200, 0, 400, SCREEN_HEIGHT))

      # 1. Draw the "Bell Curve" Center (Safe Zone)
        # 440 to 840 is the middle 400 pixels of a 1280 screen
        pygame.draw.rect(screen, GRAY, (440, 0, 400, HEIGHT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SPAWN_EVENT:
                new_point = DataPoint(WIDTH)
                points_group.add(new_point)

#         # 2. Update Points
#         points.update()

#         # # 3. Game Logic: Catching points
#         for point in points:
#         #     # If player clicks the point 
#         #     # The twist logic goes here
#             pass

#         points.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# if __name__ == "__name__":
#     main()       

# Example file showing a basic pygame "game loop"

# pygame setup


