"""Panel container for UI widgets"""

import pygame
from typing import Optional, Callable
from .widgets import Slider, Toggle, Button
from .colors import Colors


class Panel:
    """A draggable panel container for UI widgets"""
    
    def __init__(self, x: int, y: int, width: int, height: int, title: str) -> None:
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.title: str = title
        self.dragging: bool = False
        self.drag_offset: tuple[int, int] = (0, 0)
        self.widgets: list = []
        self.collapsed: bool = False
        self.header_height: int = 35
        
    def add_slider(self, label: str, min_val: float, max_val: float, 
                   initial_val: float) -> Slider:
        """Add a slider to the panel
        
        Args:
            label: Display label for the slider
            min_val: Minimum value
            max_val: Maximum value
            initial_val: Initial value
            
        Returns:
            Slider: The created slider widget
        """
        y_offset = self.header_height + 15 + len(self.widgets) * 50
        slider = Slider(self.rect.x + 20, self.rect.y + y_offset, 
                       self.rect.width - 40, min_val, max_val, initial_val, label)
        self.widgets.append(slider)
        return slider
        
    def add_toggle(self, label: str, initial_state: bool = False) -> Toggle:
        """Add a toggle switch to the panel
        
        Args:
            label: Display label for the toggle
            initial_state: Initial state (True/False)
            
        Returns:
            Toggle: The created toggle widget
        """
        y_offset = self.header_height + 15 + len(self.widgets) * 50
        toggle = Toggle(self.rect.x + 20, self.rect.y + y_offset, label, initial_state)
        self.widgets.append(toggle)
        return toggle
        
    def add_button(self, label: str, callback: Optional[Callable[[], None]] = None) -> Button:
        """Add a button to the panel
        
        Args:
            label: Display label for the button
            callback: Function to call when button is clicked
            
        Returns:
            Button: The created button widget
        """
        y_offset = self.header_height + 15 + len(self.widgets) * 50
        button = Button(self.rect.x + 20, self.rect.y + y_offset, 
                       self.rect.width - 40, 30, label, callback)
        self.widgets.append(button)
        return button
        
    def draw(self, surface: pygame.Surface, font: pygame.font.Font, 
             title_font: pygame.font.Font) -> None:
        """Draw the panel and all its widgets"""
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
                
    def handle_event(self, event: pygame.event.Event) -> bool:
        """Handle pygame events. Returns True if event was handled."""
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