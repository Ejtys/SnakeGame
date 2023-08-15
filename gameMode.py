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
    
class SinglePlayerNoWalls(GameMode):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        Wall.wall_group.clear()
        
        #snake
        self.snake = Snake((5,5), cons.Direction.RIGHT)
        
        self.ball = BallGenerator(self.snake)
        
        #UI
        self.score_label = Label("Score: 0", (cons.WINDOW_WIDTH / 2, 17))
        
    def draw(self):
        Wall.draw_all()
        self.ball.draw()
        self.snake.draw()
        
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
            
class SinglePlayerWithWalls(SinglePlayerNoWalls):
    def __init__(self):
        super().__init__()
        Wall.create_boundry_wall()
        
class MultiPlayer(GameMode):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        Wall.wall_group.clear()
        
        #snake
        self.player1 = Snake((cons.COLS - 6, 5), cons.Direction.LEFT, "arrows")
        self.player2 = Snake((5,5), cons.Direction.RIGHT, "wsad", cons.WHITE_SNAKE_COLORS)
        
        self.ball = BallGenerator(self.player1, self.player2)
        
        #UI
        self.player1_score_label = Label("Player 1: 0", (cons.WINDOW_WIDTH -75 , 17))
        self.player2_score_label = Label("Player 2: 0", (75 , 17))
    
    def draw(self):
        Wall.draw_all()
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()
        
        self.draw_lines()
        
        self.player1_score_label.draw(self.screen)
        self.player2_score_label.draw(self.screen)
    
    def event_manager(self, event):
        self.player1.event_manager(event)
        self.player2.event_manager(event)
        self.play_again(event)
    
    def play_again(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not self.player1.is_alive or not self.player2.is_alive:
                self.player1 = Snake((cons.COLS - 6, 5), cons.Direction.LEFT, "arrows")
                self.player2 = Snake((5,5), cons.Direction.RIGHT, "wsad", cons.WHITE_SNAKE_COLORS)
        
                self.ball = BallGenerator(self.player1, self.player2)
    
    def update(self, dt):
        self.ball.update()
        self.player1.update(dt)
        self.player2.update(dt)
        self.player1.collide_with_snake(self.player2)
        self.player2.collide_with_snake(self.player1)
        self.player1_score_label.update_text(f"Player 1: {self.player1.get_score()}")
        self.player2_score_label.update_text(f"Player 2: {self.player2.get_score()}")