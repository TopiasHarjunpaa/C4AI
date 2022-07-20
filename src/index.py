import pygame
from services.clock_service import ClockService
from services.event_queue_service import EventQueueService
from ui.renderer import Renderer
from ui.ui import UI
from config import FPS, TITLE

def main():
    """Start the game.
    Read display size, set title and create classes needed for UI.
    """
    pygame.init()
    display_info = pygame.display.Info()
    display_width = display_info.current_w
    display_heigth = display_info.current_h
    display = pygame.display.set_mode((display_width, display_heigth))
    pygame.display.set_caption(TITLE)

    renderer = Renderer(display, display_width, display_heigth)
    event_queue = EventQueueService()
    clock = ClockService(FPS)
    user_interface = UI(renderer, event_queue, clock)

    user_interface.start_menu()

if __name__ == "__main__":
    main()