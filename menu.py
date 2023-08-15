import pygame
import cons
from label import Label

class Menu:
    def __init__(self, title) -> None:
        self.screen = pygame.display.get_surface()
        
        self.title = Label(title, (cons.WINDOW_WIDTH / 2, 70), 48)
        
        self.labels = []
        self.next_label_height = 150
        self.selected = 0
        
        self.active = True
    
    def activate(self):
        self.active = True
    
    
    def add_label(self, text, func = None):
        label = Label(text, (cons.WINDOW_WIDTH / 2, self.next_label_height), 36, func = func)
        label.set_selectable()
        self.labels.append(label)
        if len(self.labels) == 1:
            label.toggle_selected()
        
        self.next_label_height += 60
        
    def draw(self):
        if self.active:
            self.title.draw(self.screen)
            for label in self.labels:
                label.draw(self.screen)
    
    def update(self, dt):
        pass
    
    def event_manager(self, event):
        if self.active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.labels[self.selected].toggle_selected()
                self.selected += 1
                if self.selected >= len(self.labels):
                    self.selected = 0
                self.labels[self.selected].toggle_selected()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.labels[self.selected].toggle_selected()
                self.selected -= 1
                if self.selected < 0:
                    self.selected = len(self.labels) - 1
                self.labels[self.selected].toggle_selected()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.active = False
                    self.labels[self.selected].press_label()