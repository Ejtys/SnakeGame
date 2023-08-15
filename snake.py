import pygame
from pygame.math import Vector2 as Vector
import cons
from wall import Wall


class Snake:
    def __init__(self, cell, start_direction = cons.Direction.RIGHT, 
                 controls = None, colors = cons.RED_SNAKE_COLORS) -> None:
        self.screen = pygame.display.get_surface()
        
        self.controls = controls
        self.colors = colors
        
        self.head = pygame.Rect(self.cell_to_pos(cell), (cons.SQUARE_SIZE, cons.SQUARE_SIZE))
        
        self.init_tail(cell, start_direction)
        
        self.delta = 0
        
        self.is_alive = True
        
        self.immoratality_count_down = 0
    
    def init_tail(self, cell, start_direction):
        self.tail = []
        for x in range(4, 0, -1):
            if start_direction == cons.Direction.RIGHT:
                tail_cell = [cell[0] - x, cell[1]]
            if start_direction == cons.Direction.LEFT:
                tail_cell = [cell[0] + x, cell[1]]
            if start_direction == cons.Direction.DOWN:
                tail_cell = [cell[0], cell[1] - x]
            if start_direction == cons.Direction.UP:
                tail_cell = [cell[0], cell[1] + x]
            self.tail.append(pygame.Rect(self.cell_to_pos(tail_cell), (cons.SQUARE_SIZE, cons.SQUARE_SIZE)))
        
        self.tail_is_growing = False
        
        self.direction = start_direction
        self.next_direction = start_direction
        self.direction_list = [start_direction for _ in range(len(self.tail))]
            
        
    def cell_to_pos(self, cell):
        return [cell[0] * cons.SQUARE_SIZE, cell[1] * cons.SQUARE_SIZE]
    
    def draw(self):
        for rect in self.tail:
            pygame.draw.rect(self.screen, self.colors[1], rect)
        
        pygame.draw.rect(self.screen, self.colors[0], self.head)
    
    def move(self,dt):

        self.update_direction_on_move()

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
        
        for rect in self.tail + [self.head]:
            if rect.topleft[0] >= cons.WINDOW_WIDTH:
                rect.topleft = (0, rect.topleft[1])
            if rect.topleft[0] < 0:
                rect.topleft = (cons.WINDOW_WIDTH - cons.SQUARE_SIZE, rect.topleft[1])
            if rect.topleft[1] >= cons.WINDOW_HEIGHT:
                rect.topleft = (rect.topleft[0], 0)
            if rect.topleft[1] < 0:
                rect.topleft = (rect.topleft[0], cons.WINDOW_HEIGHT - cons.SQUARE_SIZE)
                    
    def grow(self):
        self.tail_is_growing = True
    
    def event_manager(self, event):
        if event.type == pygame.KEYDOWN:
            self.input_direction(event)
    
    def update_direction_on_move(self):
        if self.next_direction == cons.Direction.LEFT and self.next_direction != cons.Direction.RIGHT:
            self.direction = cons.Direction.LEFT
        if self.next_direction == cons.Direction.RIGHT and self.next_direction != cons.Direction.LEFT:
            self.direction = cons.Direction.RIGHT
        if self.next_direction == cons.Direction.UP and self.next_direction != cons.Direction.DOWN:
            self.direction = cons.Direction.UP
        if self.next_direction == cons.Direction.DOWN and self.next_direction != cons.Direction.UP:
            self.direction = cons.Direction.DOWN
    
    def input_direction(self, event):
        if self.controls == "arrows" or not self.controls:
            if event.key == pygame.K_LEFT and self.direction != cons.Direction.RIGHT:
                self.next_direction = cons.Direction.LEFT
            if event.key == pygame.K_RIGHT and self.direction != cons.Direction.LEFT:
                self.next_direction = cons.Direction.RIGHT
            if event.key == pygame.K_UP and self.direction != cons.Direction.DOWN:
                self.next_direction = cons.Direction.UP
            if event.key == pygame.K_DOWN and self.direction != cons.Direction.UP:
                self.next_direction = cons.Direction.DOWN
        
        if self.controls == "wsad" or not self.controls:
            if event.key == pygame.K_a and self.direction != cons.Direction.RIGHT:
                self.next_direction = cons.Direction.LEFT
            if event.key == pygame.K_d and self.direction != cons.Direction.LEFT:
                self.next_direction = cons.Direction.RIGHT
            if event.key == pygame.K_w and self.direction != cons.Direction.DOWN:
                self.next_direction = cons.Direction.UP
            if event.key == pygame.K_s and self.direction != cons.Direction.UP:
                self.next_direction = cons.Direction.DOWN

    def get_score(self):
        return len(self.tail)

    def self_collide(self):
        for rect in self.tail:
            if self.head.colliderect(rect):
                self.is_alive = False
    
    def collide_with_wall(self):
        if Wall.collide_with_any(self.head):
            self.is_alive = False

    def collide_with_snake(self, snake:"Snake"):
        for rect in snake.tail:
            if self.head.colliderect(rect):
                if self.immoratality_count_down > 0:
                    return
                if self.tail:
                    del self.tail[0]
                    del self.direction_list[0]
                    self.immoratality_count_down = 1
                if not self.tail:
                    self.is_alive = False
                return
        
    def update(self, dt):
        self.immoratality_count_down -= 1
        self.self_collide()
        self.collide_with_wall()
        if self.is_alive:
            self.move(dt)
        else:
            pygame.event.post(pygame.event.Event(cons.GAME_OVER_EVENT))
            
        