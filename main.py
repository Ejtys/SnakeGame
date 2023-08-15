import pygame, sys
import cons
from gameMode import SinglePlayerWithWalls, SinglePlayerNoWalls

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
        pygame.display.set_caption(cons.TITLE)

        #clock
        self.clock = pygame.time.Clock()
        self.prev_time = pygame.time.get_ticks()
        
        self.game_mode = SinglePlayerNoWalls()
        
    def quit_game(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def event_loop(self):
        for event in pygame.event.get():
            self.quit_game(event)
            self.game_mode.event_manager(event)
    
    def get_delta_time(self):
        current_time = pygame.time.get_ticks()
        dt = (pygame.time.get_ticks() - self.prev_time) / 1000.0  # Convert to seconds
        self.prev_time = current_time
        return dt
    
    def draw(self):
        self.screen.fill(cons.BACKGROUND_COLOR)
        
        self.game_mode.draw()
              
        pygame.display.flip()
    
    def run(self):
        while True:
            dt = self.get_delta_time()
            
            self.event_loop()
            
            self.game_mode.update(dt)
            
            self.draw()
            
            self.clock.tick()
                
if __name__ == "__main__":
    Game().run()