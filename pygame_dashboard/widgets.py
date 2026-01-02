"""UI widget components"""

import pygame
from typing import Optional, Callable
from .colors import Colors


class Slider:
    """A draggable slider widget for numeric values"""
    
    def __init__(self, x: int, y: int, width: int, min_val: float, max_val: float, 
                 initial_val: float, label: str) -> None:
        self.rect: pygame.Rect = pygame.Rect(x, y, width, 20)
        self.min_val: float = min_val
        self.max_val: float = max_val
        self.value: float = initial_val
        self.label: str = label
        self.dragging: bool = False
        
    def draw(self, surface: pygame.Surface, font: pygame.font.Font) -> None:
        """Draw the slider on the surface"""
        label_surf = font.render(f"{self.label}: {self.value:.2f}", True, Colors.TEXT)
        surface.blit(label_surf, (self.rect.x, self.rect.y - 20))
        
        pygame.draw.rect(surface, Colors.SLIDER_TRACK, self.rect, border_radius=3)
        
        ratio = (self.value - self.min_val) / (self.max_val - self.min_val)
        handle_x = self.rect.x + int(ratio * self.rect.width)
        handle_rect = pygame.Rect(handle_x - 5, self.rect.y - 3, 10, 26)
        pygame.draw.rect(surface, Colors.ACCENT, handle_rect, border_radius=3)
        
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle pygame events"""
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
    
    def __init__(self, x: int, y: int, label: str, initial_state: bool = False) -> None:
        self.rect: pygame.Rect = pygame.Rect(x, y, 40, 20)
        self.label: str = label
        self.state: bool = initial_state
        
    def draw(self, surface: pygame.Surface, font: pygame.font.Font) -> None:
        """Draw the toggle on the surface"""
        label_surf = font.render(self.label, True, Colors.TEXT)
        surface.blit(label_surf, (self.rect.x + 50, self.rect.y))
        
        color = Colors.ACCENT if self.state else Colors.TOGGLE_OFF
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        
        circle_x = self.rect.x + 28 if self.state else self.rect.x + 12
        pygame.draw.circle(surface, (240, 240, 240), (circle_x, self.rect.centery), 8)
        
    def handle_event(self, event: pygame.event.Event) -> bool:
        """Handle pygame events. Returns True if state changed."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.state = not self.state
                return True
        return False


class Button:
    """A clickable button widget"""
    
    def __init__(self, x: int, y: int, width: int, height: int, label: str, 
                 callback: Optional[Callable[[], None]] = None) -> None:
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.label: str = label
        self.callback: Optional[Callable[[], None]] = callback
        self.hovered: bool = False
        
    def draw(self, surface: pygame.Surface, font: pygame.font.Font) -> None:
        """Draw the button on the surface"""
        color = Colors.ACCENT if self.hovered else Colors.SLIDER_TRACK
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        
        text_surf = font.render(self.label, True, Colors.TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def handle_event(self, event: pygame.event.Event) -> bool:
        """Handle pygame events. Returns True if button was clicked."""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False