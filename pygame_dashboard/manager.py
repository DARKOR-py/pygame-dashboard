"""Dashboard manager for handling multiple panels"""

import pygame
from typing import List
from .panel import Panel


class DashboardManager:
    """Manages multiple panels and handles rendering/events"""
    
    def __init__(self) -> None:
        self.panels: List[Panel] = []
        self.font: pygame.font.Font = pygame.font.Font(None, 24)
        self.title_font: pygame.font.Font = pygame.font.Font(None, 28)
        
    def add_panel(self, panel: Panel) -> Panel:
        """Add a panel to the dashboard
        
        Args:
            panel: The panel to add
            
        Returns:
            Panel: The added panel
        """
        self.panels.append(panel)
        return panel
        
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle pygame events for all panels
        
        Args:
            event: The pygame event to handle
        """
        for panel in reversed(self.panels):
            if panel.handle_event(event):
                self.panels.remove(panel)
                self.panels.append(panel)
                break
                
    def draw(self, surface: pygame.Surface) -> None:
        """Draw all panels on the surface
        
        Args:
            surface: The pygame surface to draw on
        """
        for panel in self.panels:
            panel.draw(surface, self.font, self.title_font)
            
    def set_fonts(self, font_size: int = 24, title_font_size: int = 28) -> None:
        """Change the font sizes
        
        Args:
            font_size: Size for widget text
            title_font_size: Size for panel titles
        """
        self.font = pygame.font.Font(None, font_size)
        self.title_font = pygame.font.Font(None, title_font_size)