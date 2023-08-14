import pygame, random
import cons
from snake import Snake

class BallGenerator:
    def __init__(self, snake:Snake):
        self.screen = pygame.display.get_surface()
        
        self.snake = snake
        
        self.ball = None
        self.generate_ball()
        
    def generate_ball(self):
        x = int(random.randint(0, cons.WINDOW_WIDTH) / cons.SQUARE_SIZE) * cons.SQUARE_SIZE
        y = int(random.randint(0, cons.WINDOW_HEIGHT) / cons.SQUARE_SIZE) * cons.SQUARE_SIZE
        
        self.ball = pygame.Rect((x,y), (cons.SQUARE_SIZE, cons.SQUARE_SIZE))
        
    def draw(self):
        pygame.draw.rect(self.screen, "yellow", self.ball)
        
    def update(self):
        pass