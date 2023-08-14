import pygame
import cons



class Snake:
    def __init__(self, cell) -> None:
        self.screen = pygame.display.get_surface()
        self.head = pygame.Rect(self.cell_to_pos(cell), (cons.SQUARE_SIZE, cons.SQUARE_SIZE))
        
    def cell_to_pos(self, cell):
        return cell[0] * cons.SQUARE_SIZE, cell[1] * cons.SQUARE_SIZE
    
    def draw(self):
        pygame.draw.rect(self.screen, "red", self.head)