"""UI widget components"""

import pygame
from .colors import Colors


class Slider:
    """A draggable slider widget for numeric values"""
    
    def __init__(self, x, y, width, min_val, max_val, initial_val, label):
        self.rect = pygame.Rect(x, y, width, 20)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.label = label
        self.dragging = False
        
    def draw(self, surface, font):
        label_surf = font.render(f"{self.label}: {self.value:.2f}", True, Colors.TEXT)
        surface.blit(label_surf, (self.rect.x, self.rect.y - 20))
        
        pygame.draw.rect(surface, Colors.SLIDER_TRACK, self.rect, border_radius=3)
        
        ratio = (self.value - self.min_val) / (self.max_val - self.min_val)
        handle_x = self.rect.x + int(ratio * self.rect.width)
        handle_rect = pygame.Rect(handle_x - 5, self.rect.y - 3, 10, 26)
        pygame.draw.rect(surface, Colors.ACCENT, handle_rect, border_radius=3)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_x = self.rect.x + int((self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
            handle_rect = pygame.Rect(handle_x - 5, self.rect.y - 3, 10, 26)
            if handle_rect.collidepoint(event.pos):
                self.dragging = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            rel_x = event.pos[0] - self.rect.x
            ratio = max(0, min(1, rel_x / self.rect.width))
            self.value = self.min_val + ratio * (self.max_val - self.min_val)


class Toggle:
    """A toggle switch widget for boolean values"""
    
    def __init__(self, x, y, label, initial_state=False):
        self.rect = pygame.Rect(x, y, 40, 20)
        self.label = label
        self.state = initial_state
        
    def draw(self, surface, font):
        label_surf = font.render(self.label, True, Colors.TEXT)
        surface.blit(label_surf, (self.rect.x + 50, self.rect.y))
        
        color = Colors.ACCENT if self.state else Colors.TOGGLE_OFF
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        
        circle_x = self.rect.x + 28 if self.state else self.rect.x + 12
        pygame.draw.circle(surface, (240, 240, 240), (circle_x, self.rect.centery), 8)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.state = not self.state
                return True
        return False


class Button:
    """A clickable button widget"""
    
    def __init__(self, x, y, width, height, label, callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.callback = callback
        self.hovered = False
        
    def draw(self, surface, font):
        color = Colors.ACCENT if self.hovered else Colors.SLIDER_TRACK
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        
        text_surf = font.render(self.label, True, Colors.TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False