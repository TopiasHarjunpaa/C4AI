# Project implementation

## Architecture

### General structure

General structure of the software consist from the following packages:

1. User interface `ui`
2. Logic services `services`
4. Datastructures and object `entities`

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/class_diagram.png" width="1000">

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

**Game services** are handled by the classes [GameService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/game_service.py) and [BoardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/board_service.py). These are handling updating game situations such as keeping up the board situations, player turns and terminal situations. Primary functionalities are:

* `GameService` -class has `start_gameloop()` -method which starts the game loop, initializes the game situation, follows the player commands and forwards turns for the AI services.
* During the initialization `BoardService` -class uses `reset()` -method to clear the game board.
* During the game loop `GameService` -class is checking the player keyboard inputs with `_check_events()` -method, calculating next move for the AI player with `_calculate_next_move()` -method. Both methods are mainly used to determine next move so that `BoardService` -class can add and update the game board using the methos `add_coin()` and `update()`.

**Situation services** are handled by classes [SituationService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/situation_service.py) and [BitboardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/bitboard_service.py). Both are used for similar kind of purposes, but `SituationService` is primarily used for the list matrix operations which are used for the Game services and intermediate level AI. `BitboardService` is used for the binary operations which is for the advanced level AI. Primary functionalities are:

* Checking the available columns or locations at the game board are handled by `SituationService` method `get_available_locations_ranked(grid)` and `BitboardService` method `get_available_non_losing_columns(position, player_index, check_symmetry)`. First one returns all possible available locations (both row and column indexes) and ranks them in order starting from the middlest column. Second one is a bit more advanced and leaves out of symmetrical columns and columns which are leading to losing the game next round. Instead of returning the location, it will only return column index.
* Checking the terminal situations are handled by `SituationService` method `check_terminal_node(grid, player_number)` and `BitboardService` method `check_terminal_node(position, player_index)`. Both methods are checking if game has ended for the win or draw and returns heuristic value according to the situation. `SituationService` uses infinite values for winning situations and `BitboardService` uses the values which are depended how many game coins are placed on the board ie. promotes AI for looking the fastest way of winning.
* Keeping track of how many coins are placed on the game board is handled by `SituationService` method `count_free_slots(grid)` and `BitboardService` method `count_coins(player_bitboard)`. As the name refers, the first one counts how many free slots are at the game board when the last one counts how many game coins has placed on a board for each player.
* `BitboardService` -class has also `convert_to_position(grid)` -method which converts the list matrix from the current game board into bitboard. This is needed because the game services are keeping track of the game board in list matrix format.

**Heuristic services** are handled by [HeuristicService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/heuristic_service.py) -class which is used for the heuristic calculations used by AI services. Primary functionalities are:

* Most of the methods are used by intermediate AI to evaluate list matrix and calculate score for several directions such as `_count_values(oc, player_number)`, `_get_positional_values(grid, player_number)`, `_get_vertical_values(grid, player_number)` etc. Total score for intermediate AI will be calculated with method `calculate_heuristic_value(grid, player_number)`.
* Heuristic value for the advanced AI is calculated with method `calculate_heuristic_value_with_bitboards(position, player_index)` while necessary evaluation of the bitboard has been made with `BitboardService` -class method `check_three_connect(player_bitboard, opponent_bitboard)`.


**AI services** are handled by [AiService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/ai_service.py) -class which is to calculate next move for different level AI opponents. Primary functionalities are:

* Next move calculation for the basic AI is handled by `calculate_next_move_basic(grid, player_number)` method which simply loops through all possible moves, calculates heuristic values for each move and returns the move which gets the highest heuristic value. This is basically just very stupid AI and does not give any match against the human player.
* Next move calculation for the intermediate AI is handled by `calculate_next_move_minimax(grid, player_number, depth)` method which uses Minimax algorithm [^1] and alpha beta pruning [^2] with default depth of 7 to calculate next move. This is actually playing suprisingly well against the human player and is already quite hard to beat for the average player.
* Next move calculation for the advanced AI is handled by `calculate_next_move_id_minimax(grid, player_number, timeout, max_depth)` method which uses iterative deepening and Minimax algorithm to calculate next move within certain time limit as deep as it gets. There are also several optimisations made in order to reach better search depth:

    * List matrix presentation has been converted into bitboard presentation [^4]
    * Transposition table to prevent recalcution of the similar game situation
    * Improved move exploration ordering which uses heuristic calculation results and removes losing move paths
    * Skips symmetrical paths

    *Ideas for several optimisation methods used for the advanced AI has been taken from the Pascal Pons blog post: Solving connect 4: How to build a perfect AI* [^3]

## Space and time complexity

Time complexity of simple Minimax algorithm is $O(b^d)$ where $b$ is a branching factor ie. number of possible moves and $d$ is a search depth. Connect four game board has board with 6 rows and 7 columns which means that maximum number of possible moves $b=7$ and maximum search depth $d=6\times7=42$. 
Time complexity can be reduced by alpha-beta pruning. With optimal move ordering ie. best moves are always searched first, time complexity can be reduced up to $O(\sqrt(b^d))$ which means that the search depth can be doubled with same amount of computation compared for the simple Minimax algorithm. If the moves are considered at the random order, time complexity is $O((b - 1 + \sqrt(b^2 + 14b + 1) / 4)^d)$. [^2] 
Space complexity is the same for both Minimax and Minimax with alpha-beta pruning $O(bd)$. [^5]

### Sources:

[^1]: Wikipedia, [Minimax](https://en.wikipedia.org/wiki/Minimax), readed 19.7.2022  
[^2]: Wikipedia, [Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha_beta_pruning), readed 19.7.2022   
[^3]: Dominikus Herzberg [Bitboards and Connect Four](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md), readed 5.8.2022
[^4]: Pascal Pons 2019 [Solving connect 4: How to build a perfect AI](http://blog.gamesolver.org/), readed 19.7.2022
[^5]: GitBook [Property of alpha-beta pruning algorithm](https://ai-master.gitbooks.io/adversarial-search/content/property-of-alpha-beta-pruning-algorithm.html), readed 22.8.2022
