import pygame, random
import cons
from snake import Snake
from wall import Wall

class BallGenerator:
    def __init__(self, snake:Snake, snake2:Snake = None):
        self.screen = pygame.display.get_surface()
        
        self.snakes = [snake]
        if snake2:
            self.snakes.append(snake2)
            
        self.colliding_snake = None
        
        self.ball = None
        self.generate_ball()
        
    def generate_ball(self):
        x = int(random.randint(0, cons.WINDOW_WIDTH -1) / cons.SQUARE_SIZE) * cons.SQUARE_SIZE
        y = int(random.randint(0, cons.WINDOW_HEIGHT -1) / cons.SQUARE_SIZE) * cons.SQUARE_SIZE
        
        self.ball = pygame.Rect((x,y), (cons.SQUARE_SIZE, cons.SQUARE_SIZE))
        if self.collide_with_snake() or Wall.collide_with_any(self.ball):
            self.generate_ball()
    
    def collide_with_snake(self):
        for snake in self.snakes:
            for rect in snake.tail + [snake.head]:
                if self.ball.colliderect(rect):
                    self.colliding_snake = snake
                    return True
        self.colliding_snake = None
        return False
    
    def on_collide_with_snake(self):
        if self.collide_with_snake():
            self.colliding_snake.grow()
            self.generate_ball()
        
    def draw(self):
        pygame.draw.rect(self.screen, "yellow", self.ball)
        
    def update(self):
        self.on_collide_with_snake()