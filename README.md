# pygame-dashboard

A simple, lightweight UI library for pygame projects. Create draggable panels with sliders, toggles, and buttons.

## Installation

```bash
pip install pygame-dashboard
```

## Quick Start

```python
import pygame
from pygame_dashboard import Panel, DashboardManager

pygame.init()
screen = pygame.display.set_mode((800, 600))
dashboard = DashboardManager()

# Create a panel
panel = Panel(50, 50, 300, 200, "Settings")
gravity = panel.add_slider("Gravity", 0, 20, 9.8)
collisions = panel.add_toggle("Collisions", True)
dashboard.add_panel(panel)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        dashboard.handle_event(event)
    
    screen.fill((20, 20, 25))
    dashboard.draw(screen)
    pygame.display.flip()

pygame.quit()
```

## Features

- ✅ Draggable panels
- ✅ Collapsible panels
- ✅ Sliders for numeric values
- ✅ Toggle switches
- ✅ Buttons with callbacks
- ✅ Zero configuration needed

## License

MIT License