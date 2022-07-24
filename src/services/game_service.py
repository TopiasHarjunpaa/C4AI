import random
import pygame


PLAYER = 1
AI_BASIC = 2
AI_ADVANCED = 3
PLAYER_TYPES = {PLAYER: "Player",
                AI_BASIC: "AI (basic)",
                AI_ADVANCED: "AI (advanced)"}

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
        Sets default player setup. Both players can be chosen to be AI or human.

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
        self._player_setup = {1: PLAYER, 2: AI_BASIC}

    def start_gameloop(self):
        """Starts the game loop and sets playing to true ie. game has started.
        Checks the events for human players and calculates the moves for AI players.
        Checks the playing status and renders the display during the loop.
        """

        self.player_number = 1
        self.playing = True
        self._board.reset()
        while self.playing:
            self._clock.tick()
            if self._player_setup[self.player_number] == 1:
                self._check_events()
            else:
                self._calculate_next_move()
            self._board.update()
            self._render()
        self._menu.show_game_ended_view(self.player_number)

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
                    self._board.print_grid()
                if event.key in accepted_keys:
                    if self._board.add_coin(event.key - 49, self.player_number):
                        if self._board.check_win(self.player_number):
                            self.playing = False
                        else:
                            self._change_turn()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self._menu.start_menu()

    def _calculate_next_move(self):
        """Calculates and creates the next move for AI player.
        """

        available_columns = self._board.get_available_columns()
        column = random.choice(available_columns)
        self._board.add_coin(column, self.player_number)
        if self._board.check_win(self.player_number):
            self.playing = False
        else:
            self._change_turn()

    def _change_turn(self):
        """Changes turns between player 1 and player 2.
        """

        if self.player_number == 1:
            self.player_number = 2
        else:
            self.player_number = 1

    def get_player_setup(self):
        """Gives player setup names as a tuple with two player name strings.

        Returns:
            tuple: First player name (str) and second player name (str)
        """

        first = PLAYER_TYPES[self._player_setup[1]]
        second = PLAYER_TYPES[self._player_setup[2]]
        return (first, second)

    def change_player_setup(self, number):
        """Changes the player setup. Player one and player two can
        have several types, suchs as player or AI which can be changed
        from game setup manu. Rotates between values 1,2,3 which indicates
        each player type (player and two AI types).

        Args:
            number (int): Player number (1 or 2) which type will be changed
        """

        self._player_setup[number] = self._player_setup[number] % 3 + 1

    def _render(self):
        """Call renderer object which renders the display.
        """

        self._renderer.render_game(self._board, self.player_number)

    def _render_game_ended(self):
        """Call renderer object which renders the game ended screen.
        """

        self._renderer.render_game_ended(self._board, self.player_number)
