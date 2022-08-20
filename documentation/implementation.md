# Project implementation

## Architecture

### General structure

General structure of the software consist from the following packages:

1. User interface `ui`
2. Logic services `services`
4. Datastructures and object `entities`

Placeholder for picture

### UI

User interface are handled with the packet `ui`, which contains following views:

1. Start menu `MenuView`
2. Settings `SetupView`

Each view has been implemented as a own class. Views are handled with [UI](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/ui/ui.py) -class which uses drawing class [Renderer](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/ui/renderer.py).

### Logic services


Logic services are handled with the packet `services`, which has the following tasks:

1. Game services
2. Situation services
3. Heuristic services
4. AI services

Game services are handled by classes [GameService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/game_service.py) and [BoardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/board_service.py). These are handling updating game situations such as keeping up the board situations, player turns and terminal situations. Primary functionalities are:

* `GameService` -class has `start_gameloop()` -method which starts the game loop, initializes the game situation, follows the player commands and forwards turns for the AI services.
* During the initialization `BoardService` -class uses `reset()` -method to clear the game board.
* During the game loop `GameService` -class is checking the player keyboard inputs with `_check_events()` -method, calculating next move for the AI player with `_calculate_next_move()` -method. Both methods are mainly used to determine next move so that `BoardService` -class can add and update the game board using the methos `add_coin()` and `update()`.

Situation services are handled by classes [SituationService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/situation_service.py) and [BitboardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/bitboard_service.py). Both are used for similar kind of purposes, but `SituationService` is primarily used for the list matrix operations which are used for the Game services and intermediate level AI. `BitboardService` is used for the binary operations which is for the advanced level AI. Primary functionalities are:

* Checking the available columns or locations at the game board are handled by `SituationService` method `get_available_locations_ranked(grid)` and `BitboardService` method `get_available_non_losing_columns(position, player_index, check_symmetry)`. First one returns all possible available locations (both row and column indexes) and ranks them in order starting from the middlest column. Second one is a bit more advanced and leaves out of symmetrical columns and columns which are leading to losing the game next round. Instead of returning the location, it will only return column index.
* Checking the terminal situations are handled by `SituationService` method `check_terminal_node(grid, player_number)` and `BitboardService` method `check_terminal_node(position, player_index)`. Both methods are checking if game has ended for the win or draw and returns heuristic value according to the situation. `SituationService` uses infinite values for winning situations and `BitboardService` uses the values which are depended how many game coins are placed on the board ie. promotes AI for looking the fastest way of winning.
* Keeping track of how many coins are placed on the game board is handled by `SituationService` method `count_free_slots(grid)` and `BitboardService` method `count_coins(player_bitboard)`. As the name refers, the first one counts how many free slots are at the game board when the last one counts how many game coins has placed on a board for each player.
* `BitboardService` -class has also `convert_to_position(grid)` -method which converts the list matrix from the current game board into bitboard. This is needed because the game services are keeping track of the game board in list matrix format.

Heuristic services are handled by [HeuristicService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/heuristic_service.py) -class which is used for the heuristic calculations used by AI services. Primary functionalities are:

* To be added later...

AI services are handled by [AiService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/ai_service.py) -class which is to calculate next move for different level AI opponents. Primary functionalities are:

* To be added later...

## Space and time complexity

To be added later...

## Sources:

To be formated later...

[Minimax (Wikipedia)](https://en.wikipedia.org/wiki/Minimax)  
[Alpha-beta pruning (Wikipedia)](https://en.wikipedia.org/wiki/Alpha_beta_pruning)  
[Solving connect 4: How to build a perfect AI](http://blog.gamesolver.org/)  
[Bitboards and Connect Four document](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md)