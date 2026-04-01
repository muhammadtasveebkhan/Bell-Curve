import pygame
import os 
import random
from sprites import DataPoint

# Project Path Logic 
GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def get_asset_path(filename:str) -> str:
    return os.path.join(GAME_PATH,"assets", filename)

#Initializing Pygame

