import pygame


class GameService:
    """A class to represent game loop services.

    Attributes:
        menu: UI object
        board: Board object.
        renderer: Renderer object.
        event_queue: Event_queue object.
        clock: Clock object.
    """

    def __init__(self, menu, board, renderer, event_queue, clock):
        """Constructs all the necessary attributes for the game service object.
        Sets player number to 1 ie. player one starts.
        Sets playing to false ie. game has not yet started.

        Args:
            menu (UI): UI object
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
        self._menu = menu
        self.player_number = 1

    def start_gameloop(self):
        """Starts the game loop and sets playing to true ie. game has started.
        Check events, playing status and renders the display during the loop.
        """

        self.playing = True
        self._board.reset()
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
        Places a coin to the certain column according to key number between 1-7
        and translates the input to indexes between 0-6.
        Show start menu when player presses escape.
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
                    if self._board.add_coin(event.key - 49, self.player_number):
                        self._change_turn()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self._menu.start_menu()

    def _change_turn(self):
        """Changes turns between player 1 and player 2.
        """

        if self.player_number == 1:
            self.player_number = 2
        else:
            self.player_number = 1

    def _render(self):
        """Call renderer object which renders the display.
        """

        self._renderer.render_game(self._board)
