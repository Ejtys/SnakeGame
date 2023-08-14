import pygame
from pygame.math import Vector2 as Vector
from enum import Enum

TITLE = "Snake"

ROWS = 16
COLS = 24
SQUARE_SIZE = 32
WINDOW_WIDTH = COLS * SQUARE_SIZE
WINDOW_HEIGHT = ROWS * SQUARE_SIZE


LINE_COLOR = pygame.Color("black")


BACKGROUND_COLOR = pygame.Color("gray")

SPEED = 0.1

class Direction(Enum):
    UP = Vector(0, -SQUARE_SIZE)
    DOWN = Vector(0, SQUARE_SIZE)
    LEFT = Vector(-SQUARE_SIZE, 0)
    RIGHT = Vector(SQUARE_SIZE, 0)