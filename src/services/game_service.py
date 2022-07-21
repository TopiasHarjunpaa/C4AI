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
        self.player_number = 1
        self._board.__init__(self._renderer.width, self._renderer.height)
        while self.playing:
            self._clock.tick()
            self._check_events()
            self._board.update()
            if self._board.check_win(self.player_number):
                # Just for testing
                self.playing = False
                print(f"Player {self.player_number} won!")
            self._render()
        self._menu.start_menu()

    def _check_events(self):
        """Checks player events.
        Quits when player closes the game window.
        Calls jump when player presses space.
        Show start view when player presses escape.
        """
        accepted_keys = [pygame.K_1, pygame.K_2,
                        pygame.K_3, pygame.K_4,
                        pygame.K_5, pygame.K_6,
                        pygame.K_7]

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                self._menu.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    self._board.test_grid()
                if event.key in accepted_keys:
                    if self._board.add_token(event.key - 49, self.player_number):
                        self._change_turn()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self._menu.start_menu()

    def _change_turn(self):
        if self.player_number == 1:
            self.player_number = 2
        else:
            self.player_number = 1


    def _render(self):
        """Call renderer object which renders the display.
        """

        self._renderer.render_game(self._board)