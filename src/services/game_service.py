import pygame
from services.ai_service import AiService
from services.situation_service import SituationService
from entities.position import Position


PLAYER = 1
AI_BASIC = 2
AI_INTERMEDIATE = 3
AI_ADVANCED = 4
PLAYER_TYPES = {PLAYER: "Player",
                AI_BASIC: "AI (basic)",
                AI_INTERMEDIATE: "AI (Minimax depth 6)",
                AI_ADVANCED: "AI (Minimax opt.)"}


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
        self.draw = False
        self._menu = menu
        self.player_number = 1
        #self._player_setup = {1: AI_ADVANCED, 2: PLAYER}
        self._player_setup = {1: PLAYER, 2: AI_ADVANCED}
        #self._player_setup = {1: PLAYER, 2: AI_INTERMEDIATE}
        self._situation = SituationService(self._board)
        self.ai_service = AiService(self._situation)
        self._position = Position()

    def start_gameloop(self):
        """Starts the game loop and sets playing to true ie. game has started.
        Checks the events for human players and calculates the moves for AI players.
        Checks the playing status and renders the display during the loop.
        """

        self.player_number = 1
        self.playing = True
        self.draw = False
        self._board.reset()
        while self.playing:
            self._clock.tick()
            if self._player_setup[self.player_number] == PLAYER:
                self._check_events()
            else:
                self._calculate_next_move()
            self._board.update()
            self.render()
        self._menu.show_game_ended_view(self.draw)

    def _check_events(self):
        """Checks player events.
        Quits when player closes the game window.
        Places a coin to the certain column according to key number between 1-7
        and translates the input to column indexes between 0-6.
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
                if event.key in accepted_keys:
                    col_number = event.key - 49
                    row_number = self._situation.check_column_available(
                                                self._board.grid, col_number)
                    if row_number != -1:
                        self._board.add_coin(row_number, col_number, self.player_number)
                        self._check_terminal_situation()

                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self._menu.start_menu()

    def _calculate_next_move_basic(self):
        """Calculates one of the possible moves using heuristic calculation.
        This method is used for the basic level AI.

        Returns:
            tuple: Returns column and row indexes of the next move location
        """

        return self.ai_service.calculate_next_move_basic(
                                self._board.grid, self.player_number)

    def _calculate_next_move_intermediate(self):
        """Calculates next possible move using Minimax algorithm.
        This method is used for the intermediate level of AI.

        Returns:
            tuple: Returns column and row indexes of the next move location
        """

        return self.ai_service.calculate_next_move_minimax(
                                self._board.grid, self.player_number)

    def _calculate_next_move_advanced(self):
        """Calculates next possible move using optimised Minimax algorithm.
        This method is used for the advanced level of AI.

        Returns:
            tuple: Returns column and row indexes of the next move location
        """

        return self.ai_service.calculate_next_move_id_minimax(
                                self._position)

    def _check_terminal_situation(self):
        """Checks the terminal situation ie. current player wins or
        game has ended in draw. Uses situation service methods to
        check wheter the current player has won and stops the game loop if so.
        Sets also self.draw to true if the game has ended in draw.
        Otherwise turn will be changed for another player and game loop can continue.

        Returns:
            Boolean: Returns true if game has ended. Otherwise returns false.
        """
        if self._situation.check_win(self._board.grid, self.player_number):
            self.playing = False
            return True

        if self._situation.check_draw(self._board.grid):
            self.playing = False
            self.draw = True
            return True

        self._change_turn()
        return False

    def _calculate_next_move(self):
        """Calculates and creates the next move for AI player.
        Uses different calculation method depending
        from the AI type (basic / advanced):

        1.  Calculate the move and get row and column indexes
        2.  Adds new game coing on the board after move has been calculated.
        3.  Checks if the current player has won the game using the
            check_terminal_situation method.
        """

        location = None

        if self._player_setup[self.player_number] == AI_BASIC:
            location = self._calculate_next_move_basic()

        elif self._player_setup[self.player_number] == AI_INTERMEDIATE:
            location = self._calculate_next_move_intermediate()

        else:
            column = self._calculate_next_move_advanced()
            print(column)
            row = self._situation.check_column_available(self._board.grid, column)
            location = (row, column)

        self._board.add_coin(location[0], location[1], self.player_number)
        self._check_terminal_situation()

    def _change_turn(self):
        """Changes turns between player 1 and player 2.
        """

        self.player_number = self.player_number % 2 + 1

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
        from game setup manu. Rotates between values 1,2,3,4 which indicates
        each player type (player and three AI types).

        Args:
            number (int): Player number (1 or 2) which type will be changed
        """

        self._player_setup[number] = self._player_setup[number] % 4 + 1

    def render(self, game_ended=False, draw=False):
        """Call renderer object which renders the display.

        Args:
            game_ended (bool, optional): Renders game ended screen if set to True.
            Otherwise renders normal game screen. Defaults to False.
        """

        self._renderer.render_game(self._board, self.player_number, game_ended, draw)
