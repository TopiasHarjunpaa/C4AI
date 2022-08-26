from matplotlib import pyplot as plt
from services.board_service import BoardService
from services.situation_service import SituationService
from services.ai_service import AiService

class SimulationService:
    """A class to represent Simulation services."""

    def __init__(self, intermediate_depth=7, advanced_timeout=30):
        """Constructs all the necessary attributes for the Simulation service object.
        Services are used to simulate game between AI's
        Information suchs as rounds, depths and infos will be stored in order to plot the
        results of the simulations.

        Args:
            intermediate_depth (int, optional): Depth of the intermediate AI search. Defaults to 7.
            advanced_timeout (int, optional): Timeout limit for the advanced AI. Defaults to 30.
        """

        self._board = BoardService(640, 480)
        self._situation = SituationService(self._board)
        self._ai = AiService(self._situation)
        self._grid = self._board.grid
        self._round = 0
        self._playing = True
        self._player_number = 1
        self._game_result = ""
        self._intermediate_depth = intermediate_depth
        self._advanced_timeout = advanced_timeout
        self._rounds = [[], []]
        self._depths = [[], []]
        self._infos = ["", ""]

    def _reset_params(self):
        """Resets all parameters suchs as game situation related parameters
        and information parameters.
        """

        self._board.reset()
        self._round = 0
        self._playing = True
        self._player_number = 1
        self._game_result = ""
        self._rounds = [[], []]
        self._depths = [[], []]
        self._infos = ["", ""]

    def _change_turn(self):
        """Changes player turn
        """

        self._player_number = self._player_number % 2 + 1

    def _check_terminal_situation_and_update(self, name):
        """Checks the terminal situation ie. current player wins or
        game has ended in draw. Uses situation service methods to
        check wheter the current player has won and stops the game loop if so.
        Stores information about terminal situation if game has ended.

        Returns:
            Boolean: Returns true if game has ended. Otherwise returns false.
        """
        if self._situation.check_win(self._board.grid, self._player_number):
            self._playing = False
            self._game_result = f"{name} as player {self._player_number} has won at round {self._round}"
            return True

        if self._situation.check_draw(self._board.grid):
            self._playing = False
            self._game_result = f"Game has ended draw"
            return True

        self._change_turn()
        return False

    def _update_params(self, depth):
        """Updates information parameters

        Args:
            depth (int): Maximum search depth achieved during the simulation round
        """

        index = self._player_number - 1
        self._rounds[index].append(self._round)
        self._depths[index].append(depth)  

    def simulate_intermediate_vs_advanced(self):
        """Simulates the game against intermediate AI vs advanced AI where
        intermediate AI begins. Plots the result of the simulation.
        """

        self._reset_params()
        self._infos[0] = f"Intermediate AI with depth: {self._intermediate_depth}"
        self._infos[1] = f"Advanced AI with timeout: {self._advanced_timeout} sec"

        while self._playing:
            self._round += 1
            if self._player_number == 1:
                self._calculate_intermediate_move()
            else:
                self._calculate_advanced_move()

        self._create_plot("Search distance intermediate AI vs advanced AI")
        
    def simulate_advanced_vs_intermediate(self):
        """Simulates the game against advanced AI vs intermediate AI where
        advanced AI begins. Plots the result of the simulation.
        """

        self._reset_params()
        self._infos[0] = f"Advanced AI with timeout: {self._advanced_timeout} sec"
        self._infos[1] = f"Intermediate AI with depth: {self._intermediate_depth}"

        while self._playing:
            self._round += 1
            if self._player_number == 1:
                self._calculate_advanced_move()
            else:
                self._calculate_intermediate_move()

        self._create_plot("Search distance advanced AI vs intermediate AI")

    def simulate_advanced_vs_advanced(self):
        """Simulates the game against advanced AI's. Plots the result of the simulation.
        """

        self._reset_params()
        self._infos[0] = f"Advanced AI with timeout: {self._advanced_timeout} sec"
        self._infos[1] = f"Advanced AI with timeout: {self._advanced_timeout} sec"

        while self._playing:
            self._round += 1
            self._calculate_advanced_move()
        
        self._create_plot("Search distance advanced AI vs advanced AI")

    def _calculate_advanced_move(self):
        """Calculates next move using the advanced AI and stores the simulation information
        during the process.
        """

        result = self._ai.calculate_next_move_iterative_minimax(self._board.grid, self._player_number, self._advanced_timeout)
        print(f"results: {result} at round {self._round}")
        col = result[0]
        row = self._situation.check_available_location(self._board.grid, col)
        self._board.add_coin(row, col, self._player_number)
        depth = min(result[1] + self._round, 42)
        self._update_params(depth)
        self._check_terminal_situation_and_update("advanced AI")
    
    def _calculate_intermediate_move(self):
        """Calculates next move using the intermediate AI and stores the simulation information
        during the process.
        """

        row, col = self._ai.calculate_next_move_minimax(self._board.grid, self._player_number, self._intermediate_depth)
        self._board.add_coin(row, col, self._player_number)
        depth = min(self._intermediate_depth + self._round, 42)
        self._update_params(depth)
        self._check_terminal_situation_and_update("intermediate AI")

    def _create_plot(self, title):
        """Plots the simulation results. X-axis has round number and Y-axis has search
        distance reached per certain round. Title contains simulation name and game results.

        Args:
            title (str): Title which contains simulation name and game results.
        """

        colors = ["blue", "red"]
        for index in range(2):
            plt.plot(self._rounds[index], self._depths[index], color=colors[index], label=self._infos[index])
        plt.title(f"{title} \n {self._game_result}")
        plt.xlabel("round number")
        plt.ylabel("search distance")
        plt.legend()
        plt.grid(axis="y")
        plt.show()