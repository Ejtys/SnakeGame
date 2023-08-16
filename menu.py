import pygame
import cons
from label import Label

class Menu:
    menus = []
    def __init__(self, name, title) -> None:
        self.name = name
        self.screen = pygame.display.get_surface()
        
        self.title = Label(title, (cons.WINDOW_WIDTH / 2, 70), 48)
        
        self.labels = []
        self.next_label_height = 150
        self.selected = 0
        
        self.active = False
        
        Menu.menus.append(self)
    
    @staticmethod
    def draw_all():
        for menu in Menu.menus:
            menu.draw()
    
    @staticmethod
    def event_manager(event):
        for menu in Menu.menus:
            menu.event_loop(event)
    
    @staticmethod
    def get_menu_by_name(name) -> "Menu":
        for menu in Menu.menus:
            if menu.name == name:
                return menu
    
    @staticmethod
    def activate_by_name(name):
        for menu in Menu.menus:
            menu.deactivate()
        Menu.get_menu_by_name(name).activate()
        
    @staticmethod
    def dectivate_by_name(name):
        Menu.get_menu_by_name(name).deactivate()
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def update_title(self, title):
        self.title.update_text(title)
    
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
    
    def event_loop(self, event):
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