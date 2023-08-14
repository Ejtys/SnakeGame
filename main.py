import pygame, sys
import cons
from snake import Snake

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
        pygame.display.set_caption(cons.TITLE)

        #clock
        self.clock = pygame.time.Clock()
        self.prev_time = pygame.time.get_ticks()
        
        #support lines
        self.lines_surface = pygame.Surface((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
        self.lines_surface.set_colorkey("green")
        self.lines_surface.set_alpha(60)
        
        #snake
        self.snake = Snake((5,5))
        

    def quit_game(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def event_loop(self):
        for event in pygame.event.get():
                self.quit_game(event)
                self.snake.event_manager(event)
    
    def get_delta_time(self):
        current_time = pygame.time.get_ticks()
        dt = (pygame.time.get_ticks() - self.prev_time) / 1000.0  # Convert to seconds
        self.prev_time = current_time
        return dt
    
    def draw_lines(self):
        self.lines_surface.fill("green")
        
        for x in range(0, cons.WINDOW_WIDTH, cons.SQUARE_SIZE):
            pygame.draw.line(self.lines_surface, cons.LINE_COLOR, (x, 0) , (x, cons.WINDOW_HEIGHT), 1)
        
        for y in range(0, cons.WINDOW_HEIGHT, cons.SQUARE_SIZE):
            pygame.draw.line(self.lines_surface, cons.LINE_COLOR, (0, y) , (cons.WINDOW_WIDTH, y), 1)
        
        self.screen.blit(self.lines_surface, (0, 0))
    
    def draw(self):
        self.screen.fill(cons.BACKGROUND_COLOR)
        
        self.snake.draw()
        
        self.draw_lines()      
        pygame.display.flip()
    
    def run(self):
        while True:
            dt = self.get_delta_time()
            
            self.event_loop()
            
            self.draw()
            
            self.snake.update(dt)
            
            self.clock.tick()
                
if __name__ == "__main__":
    Game().run()