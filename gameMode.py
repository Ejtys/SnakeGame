import pygame
import cons
from wall import Wall
from snake import Snake
from ballGenerator import BallGenerator
from label import Label


class GameMode:
    def __init__(self) -> None:
        self.is_paused = False
        
        #support lines
        self.lines_surface = pygame.Surface((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
        self.lines_surface.set_colorkey("green")
        self.lines_surface.set_alpha(60)
    
    def draw_lines(self):
        self.lines_surface.fill("green")
        
        for x in range(0, cons.WINDOW_WIDTH, cons.SQUARE_SIZE):
            pygame.draw.line(self.lines_surface, cons.LINE_COLOR, (x, 0) , (x, cons.WINDOW_HEIGHT), 1)
        
        for y in range(0, cons.WINDOW_HEIGHT, cons.SQUARE_SIZE):
            pygame.draw.line(self.lines_surface, cons.LINE_COLOR, (0, y) , (cons.WINDOW_WIDTH, y), 1)
        
        self.screen.blit(self.lines_surface, (0, 0))
    
    def event_manager(self, event):
        pass
    
    def draw(self):
        pass
    
    def update(self, dt):
        pass
    
class SinglePlayerWithWalls(GameMode):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        
        Wall.create_boundry_wall()
        
        #snake
        self.snake = Snake((5,5), cons.Direction.UP)
        
        self.ball = BallGenerator(self.snake)
        
        #UI
        self.score_label = Label("Score: 0", (cons.WINDOW_WIDTH / 2, 17))
        
    def draw(self):
        Wall.draw_all()
        self.snake.draw()
        self.ball.draw()
        
        self.draw_lines()
        
        self.score_label.draw(self.screen)
        
    def event_manager(self, event):
        self.snake.event_manager(event)
        self.play_again(event)
        
    def update(self, dt):
        self.ball.update()
        self.snake.update(dt)
        self.score_label.update_text(f"Score: {self.snake.get_score()}")
        
    def play_again(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.snake.is_alive:
            self.snake = Snake((5,5))
            self.ball = BallGenerator(self.snake)
            
class SinglePlayerNoWalls(SinglePlayerWithWalls):
    def __init__(self):
        super().__init__()
        Wall.wall_group = [Wall((100,100))]