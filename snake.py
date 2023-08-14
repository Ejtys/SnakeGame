import pygame
from pygame.math import Vector2 as Vector
import cons



class Snake:
    def __init__(self, cell) -> None:
        self.screen = pygame.display.get_surface()
        self.head = pygame.Rect(self.cell_to_pos(cell), (cons.SQUARE_SIZE, cons.SQUARE_SIZE))
        
        self.tail = []
        for x in range(4, 0, -1):
            tail_cell = [cell[0] - x, cell[1]]
            self.tail.append(pygame.Rect(self.cell_to_pos(tail_cell), (cons.SQUARE_SIZE, cons.SQUARE_SIZE)))
        self.tail_is_growing = False
        
        self.direction = cons.Direction.RIGHT
        self.direction_list = [cons.Direction.RIGHT for _ in range(len(self.tail))]
        
        self.delta = 0
        
    def cell_to_pos(self, cell):
        return [cell[0] * cons.SQUARE_SIZE, cell[1] * cons.SQUARE_SIZE]
    
    def draw(self):
        pygame.draw.rect(self.screen, "red", self.head)
        for rect in self.tail:
            pygame.draw.rect(self.screen, "green", rect)
    
    def move(self,dt):
        self.delta += dt
        if self.delta >= cons.SPEED:
            self.delta -= self.delta
    
            if self.tail_is_growing:
                self.tail.append(self.head.copy())
                self.direction_list.append(self.direction)
                self.tail_is_growing = False
            else:
                for rect, direction in zip(self.tail, self.direction_list):
                    rect.topleft = Vector(rect.topleft) + direction.value
            
                del self.direction_list[0]
                self.direction_list.append(self.direction)
                
            self.head.topleft = Vector(self.head.topleft) + self.direction.value
    
    def grow(self):
        self.tail_is_growing = True
    
    def event_manager(self, event):
        if event.type == pygame.KEYDOWN:
            self.change_direction(event)
    
    def change_direction(self, event):
        if event.key == pygame.K_LEFT and self.direction != cons.Direction.RIGHT:
            self.direction = cons.Direction.LEFT
        if event.key == pygame.K_RIGHT and self.direction != cons.Direction.LEFT:
            self.direction = cons.Direction.RIGHT
        if event.key == pygame.K_UP and self.direction != cons.Direction.DOWN:
            self.direction = cons.Direction.UP
        if event.key == pygame.K_DOWN and self.direction != cons.Direction.UP:
            self.direction = cons.Direction.DOWN
    
    def update(self, dt):
        self.move(dt)