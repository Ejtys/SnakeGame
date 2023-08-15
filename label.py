import pygame

class Label:
    def __init__(self, text, position, font_size=24, color="black", font = None):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(font, font_size)
        self.color = color
        self.rect = None
        
        self.selectable = False
        self.selected = False

    def set_selectable(self):
        self.selectable = True
    
    def toggle_selected(self):
        self.selected = not self.selected

    def render(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        self.rect = text_surface.get_rect()
        self.rect.center = self.position
        screen.blit(text_surface, self.rect)
        
    def update_text(self, text):
        self.text = text
        
    def draw(self,screen):
        self.render(screen)
        self.rect = self.rect.inflate(10,10)
        if self.selectable:
            if not self.selected:
                pygame.draw.rect(screen, self.color, self.rect, 3)
            else:
                pygame.draw.rect(screen, "white", self.rect, 3)
                
        
    