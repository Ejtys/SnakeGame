import pygame, sys
import cons
from gameMode import SinglePlayerWithWalls, SinglePlayerNoWalls, MultiPlayer, GameMode
from menu import Menu

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
        pygame.display.set_caption(cons.TITLE)

        #clock
        self.clock = pygame.time.Clock()
        self.prev_time = pygame.time.get_ticks()
        
        self.game_mode = GameMode()
        
        
        main_menu = Menu("Main_menu", "Select game mode:")
        main_menu.add_label("Single player", func=(self.select_game_mode, SinglePlayerNoWalls))
        main_menu.add_label("Single player with walls", func=(self.select_game_mode, SinglePlayerWithWalls))
        main_menu.add_label("MultiPlayer", func=(self.select_game_mode, MultiPlayer))
        
        main_menu.activate()
        
        game_over_menu = Menu("Game_over_menu", "Do you want to play again?")
        game_over_menu.add_label("Play again", func=(self.play_again,))
        game_over_menu.add_label("Back to main menu", func=(Menu.activate_by_name, "Main_menu"))
        
        
    def play_again(self):
        self.game_mode.play_again()
    
    def select_game_mode(self, game_mode):
        for menu in Menu.menus:
            menu.deactivate()
        self.game_mode = game_mode()
        
    def quit_game(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def event_loop(self):
        for event in pygame.event.get():
            self.quit_game(event)
            self.game_mode.event_manager(event)
            Menu.event_manager(event)
            
            if event.type == cons.GAME_OVER_EVENT:
                self.game_mode.is_paused = True
                Menu.get_menu_by_name("Game_over_menu").activate()
    
    def get_delta_time(self):
        current_time = pygame.time.get_ticks()
        dt = (pygame.time.get_ticks() - self.prev_time) / 1000.0  # Convert to seconds
        self.prev_time = current_time
        return dt
    
    def draw(self):
        self.screen.fill(cons.BACKGROUND_COLOR)
        
        self.game_mode.draw()
        Menu.draw_all()
              
        pygame.display.flip()
    
    def run(self):
        while True:
            dt = self.get_delta_time()
            
            self.event_loop()
            
            self.game_mode.update(dt)
            
            self.draw()
            
            self.clock.tick(6)
                
if __name__ == "__main__":
    Game().run()