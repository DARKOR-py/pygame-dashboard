"""Panel container for UI widgets"""

import pygame
from .widgets import Slider, Toggle, Button
from .colors import Colors


class Panel:
    """A draggable panel container for UI widgets"""
    
    def __init__(self, x, y, width, height, title):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.dragging = False
        self.drag_offset = (0, 0)
        self.widgets = []
        self.collapsed = False
        self.header_height = 35
        
    def add_slider(self, label, min_val, max_val, initial_val):
        y_offset = self.header_height + 15 + len(self.widgets) * 50
        slider = Slider(self.rect.x + 20, self.rect.y + y_offset, 
                       self.rect.width - 40, min_val, max_val, initial_val, label)
        self.widgets.append(slider)
        return slider
        
    def add_toggle(self, label, initial_state=False):
        y_offset = self.header_height + 15 + len(self.widgets) * 50
        toggle = Toggle(self.rect.x + 20, self.rect.y + y_offset, label, initial_state)
        self.widgets.append(toggle)
        return toggle
        
    def add_button(self, label, callback=None):
        y_offset = self.header_height + 15 + len(self.widgets) * 50
        button = Button(self.rect.x + 20, self.rect.y + y_offset, 
                       self.rect.width - 40, 30, label, callback)
        self.widgets.append(button)
        return button
        
    def draw(self, surface, font, title_font):
        if self.collapsed:
            header_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.header_height)
            pygame.draw.rect(surface, Colors.PANEL_HEADER, header_rect, border_radius=5)
            title_surf = title_font.render(self.title + " [+]", True, Colors.TEXT)
            surface.blit(title_surf, (self.rect.x + 10, self.rect.y + 8))
        else:
            pygame.draw.rect(surface, Colors.PANEL, self.rect, border_radius=5)
            
            header_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.header_height)
            pygame.draw.rect(surface, Colors.PANEL_HEADER, header_rect, border_radius=5)
            
            title_surf = title_font.render(self.title + " [-]", True, Colors.TEXT)
            surface.blit(title_surf, (self.rect.x + 10, self.rect.y + 8))
            
            for widget in self.widgets:
                widget.draw(surface, font)
                
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            header_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.header_height)
            if header_rect.collidepoint(event.pos):
                if event.pos[0] > self.rect.x + self.rect.width - 50:
                    self.collapsed = not self.collapsed
                    return True
                else:
                    self.dragging = True
                    self.drag_offset = (event.pos[0] - self.rect.x, event.pos[1] - self.rect.y)
                    return True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.rect.x = event.pos[0] - self.drag_offset[0]
            self.rect.y = event.pos[1] - self.drag_offset[1]
            for i, widget in enumerate(self.widgets):
                y_offset = self.header_height + 15 + i * 50
                widget.rect.x = self.rect.x + 20
                widget.rect.y = self.rect.y + y_offset
            return True
            
        if not self.collapsed:
            for widget in self.widgets:
                widget.handle_event(event)
                
        return False