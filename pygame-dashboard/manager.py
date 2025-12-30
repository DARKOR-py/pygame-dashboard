"""Dashboard manager for handling multiple panels"""

import pygame


class DashboardManager:
    """Manages multiple panels and handles rendering/events"""
    
    def __init__(self):
        self.panels = []
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 28)
        
    def add_panel(self, panel):
        self.panels.append(panel)
        return panel
        
    def handle_event(self, event):
        for panel in reversed(self.panels):
            if panel.handle_event(event):
                self.panels.remove(panel)
                self.panels.append(panel)
                break
                
    def draw(self, surface):
        for panel in self.panels:
            panel.draw(surface, self.font, self.title_font)
            
    def set_fonts(self, font_size=24, title_font_size=28):
        self.font = pygame.font.Font(None, font_size)
        self.title_font = pygame.font.Font(None, title_font_size)