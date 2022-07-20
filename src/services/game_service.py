import pygame


class GameService:
    """A class to represent game loop services.
    Attributes:
        ui: UI object
        board: Board object.
        renderer: Renderer object.
        event_queue: Event_queue object.
        clock: Clock object.
        audio: Audio object.
    """

    def __init__(self, ui, board, renderer, event_queue, clock):
        """Constructs all the necessary attributes for the game service object.
        Args:
            ui (UI): UI object
            board (Board): Board object.
            renderer (Renderer): Renderer object.
            event_queue (EventQueueService: Event and queue service object.
            clock (Clock): Clock object.
        """

        self._clock = clock
        self._board = board
        self._renderer = renderer
        self._event_queue = event_queue
        self.playing = False
        self._menu = ui

    def start_gameloop(self):
        """Starts the game loop.
        Initialises Board object with display information.
        Check events, playing status and render the display during the loop.
        Show game over view when game has ended.
        """

        self.playing = True
        self._board.__init__(self._renderer.width, self._renderer.height)
        while self.playing:
            self._clock.tick()
            self._check_events()
            self.playing = self._board.update()
            self._render()
        self._menu.show_game_over_view()

    def _check_events(self):
        """Checks player events.
        Quits when player closes the game window.
        Calls jump when player presses space.
        Show start view when player presses escape.
        """

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                self._menu.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("test key")
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self._menu.start_menu()

    def _render(self):
        """Call renderer object which renders the display.
        """

        self._renderer.render_game(self._board)