import pygame
import cons

class Wall:
    wall_group = []
    
    def __init__(self, cell):
        self.screen = pygame.display.get_surface()
        Wall.wall_group.append(self)
        self.rect = pygame.Rect(self.cell_to_pos(cell), (cons.SQUARE_SIZE, cons.SQUARE_SIZE))      
    
    def cell_to_pos(self, cell):
        return [cell[0] * cons.SQUARE_SIZE, cell[1] * cons.SQUARE_SIZE]
    
    def draw(self):
        pygame.draw.rect(self.screen, "brown", self.rect)
        
    @staticmethod
    def create_boundry_wall():
        for x in range(cons.COLS):
            Wall((x, 0))
            Wall((x, cons.ROWS - 1))
        for y in range(cons.ROWS):
            Wall((0, y))
            Wall((cons.COLS - 1, y))
            
    @staticmethod
    def draw_all():
        if Wall.wall_group:
            for wall in Wall.wall_group:
                wall.draw()
            
    @staticmethod
    def collide_with_any(rect):
        if Wall.wall_group:
            for wall in Wall.wall_group:
                if wall.rect.colliderect(rect):
                    return True
        return False