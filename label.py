import pygame

class Label:
    def __init__(self, text, position, font_size=24, color="black", font = None):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(font, font_size)
        self.color = color

    def render(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        rect = text_surface.get_rect()
        rect.center = self.position
        screen.blit(text_surface, rect)
        
    def update_text(self, text):
        self.text = text
        
    