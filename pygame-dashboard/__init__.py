"""
pygame-dashboard - A simple UI library for pygame projects
"""

__version__ = "0.1.0"
__author__ = "Robinson Petit"

from .panel import Panel
from .widgets import Slider, Toggle, Button
from .colors import Colors
from .manager import DashboardManager

__all__ = ['Panel', 'Slider', 'Toggle', 'Button', 'Colors', 'DashboardManager']
