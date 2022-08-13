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

* GameService class `start_gameloop()`, which starts the game loop, initializes the game situation, follows the player commands and forwards turns for the AI services.
* More to be added later...

Situation services are handled by classes [SituationService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/situation_service.py) and [BitboardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/bitboard_service.py). Both are used for similar kind of purposes, but `SituationService` is primarily used for the list matrix operations which are used for the Game services and intermediate level AI `BitboardService` is used for the binary operations which is for the advanced level AI. Primary functionalities are:

* To be added later...

Heuristic services are handled by [HeuristicService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/heuristic_service.py) class which is used for the heuristic calculations used by AI services. Primary functionalities are:

* To be added later...

AI services are handled by [AiService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/services/ai_service.py) class which is to calculate next move for different level AI opponents. Primary functionalities are:

* To be added later...

## Space and time complexity

To be added later...

## Sources:

To be formated later...

[Minimax (Wikipedia)](https://en.wikipedia.org/wiki/Minimax)  
[Alpha-beta pruning (Wikipedia)](https://en.wikipedia.org/wiki/Alpha_beta_pruning)  
[Solving connect 4: How to build a perfect AI](http://blog.gamesolver.org/)  
[Bitboards and Connect Four document](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md)