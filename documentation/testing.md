# Testing document

## Unit and integration testing

### Entities classes

Most of the `Entities` class testing has been made at the integration test level. The following test classes has been made to test entities:

1. [TestSprites](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/entities/sprites_test.py) -class  is used for testing initialization of the game board, drawing new coins and adding them to the corresponding sprite groups.

    *Note. These tests could be considered trivial ones and perhaps test wouldn't be necessary. However, at the earlier stage of the project, these were invented in a different way and I decided to keep these tests instead of deleting them*

2. [TestPosition](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/entities/position_test.py) -class is used for testing binary operations for the `Position` class such as making a move and returning available columns.

3. [TestTranspositionTable](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/entities/transposition_table_test.py) -class is used for testing key check operation for the Transposition class.

### Service classes

The following test classes has been made to test services:

1.  [TestAiService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/ai_service_test.py) -class is mainly used for checking next move calculations for different AI's. These tests have primary focus on terminal situations as those can be quite clearly determined if the move is either right or wrong. This test class also contains some tests for column order sorting used by advanced AI.

2.  [TestBitboardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/bitboard_service_test.py) -class is used for testing binary operations for the `BitboardService` class. This class contains tests for checking terminal situations, finding a open three connects and symmetry checks.

3.  [TestSituationService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/situation_service_test.py) -class is used for testing list matrix operations for the `SituationService` class. Tests are checking similar functionalities than `TestBitboardService` and `TestPosition` are doing suchs as checking terminal situations and returning available columns.

4.  [TestHeuristicService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/heuristic_service_test.py) -class is used for testing heuristic value calculations for the `HeuristicService` class. Most of the methods for `HeuristicService` and therefore tests as well are checking evaluation of list matrix and calculation of score for different directions such as vertical, horizontal and diagonal directions. There are several tests made for these methods and the main tests for calculating total heuristic values are handled by the methods `test_heuristic_value_returns_correct_value` and `test_heuristic_value_with_bitboards_returns_correct_value()`. First one is used for the intermediate AI calculation using the list matrix and the second one is used for the advanced AI calculation using the bitboards. Evaluation of the bitboard has been made with `BitboardService` -class which tests are carried out with `TestBitboardService` mentioned above.

5.  [TestBoardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/board_service_test.py) -class is used for testing game board operation for the `BoardService` -class. Tests are checking if the game board and game coins are updated properly and the reseting of the board works.

6.  [TestGameService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/game_service_test.py) -class is used for testing game loop operations for the `GameService` -class. Tests are checking that the game loop starts and ends as intended, key presses are working and the player setup can be changed and updated properly. In order to easily test `GameService` -class, it uses stub classes which are unnecessary from the testing perspective.

    Stub classes used:

    * `StubClock`
    * `StubEventQueue`
    * `StubRenderer`
    * `StubAudio`
    * `StubUI`

Many service classes has multiple methods which keeps track of the game situation. In order to test different game situation, [test_grids.py](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/test_grids.py) and [test_locs.py](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/test_locs.py) has been created. `Test grids` contains different board setups and `Test locs` ie. *lines of connects* contains different setups for Four Connect testing. These premade setups are arrays of length 4 containing integers 0, 1 and 2.

## Test coverage report

Coverage report can be generated using the command:

```
poetry run invoke coverage-report
```

Report will be generated into the folder named `htmlcov`. Coverage report can be also found from the [Codecov](https://app.codecov.io/gh/TopiasHarjunpaa/C4AI). Some of the files are left out from the coverage report such as files related to the UI and testing along with configuration-, simulation- and index- files.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/coverage_report.png" width="700">

Methods which were not tested: 
* Trivial methods, such as Getters, Setters and few pygame event key checks
* Printing methods
* AI move calculations methods in `GameService` class which are already tested in `AiService` class.

## Simulations

### Simulation instructions

There are three kinds of simulations available. Each simulation runs three different game scenarios against AI's which results will be plotted after each scenario has finished:
- Intermediate AI vs advanced AI
- Advanced AI vs intermediate AI
- Advanced AI vs advanced AI


First simulation sets search depth of intermediate AI to 5 and timeout limit for advanced AI to 0.5 seconds. This simulation takes less than 30 seconds to complete. Simulation can be executed using the command:

```
poetry run invoke simulate-fast
```

Second simulation sets search depth of intermediate AI to 7 and timeout limit for advanced AI to 5 seconds. This simulation takes less than 2 minutes to complete. Simulation can be executed using the command:

```
poetry run invoke simulate-normal
```

Third simulation sets search depth of intermediate AI to 7 and timeout limit for advanced AI to 30 seconds. This simulation takes less than 20 minutes to complete. Simulation can be executed using the command:

```
poetry run invoke simulate-full
```

### Simulation results

The following results has been obtained from the full simulations where intermediate AI uses normal Minimax algorithm and alpha-beta pruning with constant depth of 7 while advanced AI uses 30 second soft timeout limit for the iterative deepening Minimax and alpha-beta pruning.

Plots indicates how many rounds the game has lasted before terminal situation, who has won and how far has the search depth reached during each round. Blue line is the first player and red line is the second player.

#### Advanced AI vs advanced AI

First player wins when two similar advanced AI's plays against each other. Both AI's can reach the depth which is little bit less than 20 during the first rounds and they can see the outcome of the game at around round 15. In perfect game, there will be game coins placed in the middle column during the first rounds, which the AI's are doing even without seeing the full game during these rounds. This means that there will be roughly 10 rounds where neither of these AI will be playing perfect game and roughly 30 rounds while they are playing perfectly.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/simulation_advanced30_vs_advanced30.png" width="500">

#### Intermediate AI vs advanced AI

Advanced AI wins when it is playing against intermediate AI which is starting the game. Intermediate AI uses search depth of 7 constantly from the beginning of the game which means that it can only get slightly more information after each round and can see outcome of the game only 7 rounds before losing the game. On this simulation advanced AI can see maximum depth (42) at round 18 and outcome of the game (win at round 30) at round 14. Advanced AI is not playing perfectly during the rounds 8, 10 and 12 but it is still enough for the victory as intermediate AI is not playing as well as the advanced one.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/simulation_intermediate7_vs_advanced30.png" width="500">

**Advanced AI vs intermediate AI**

Advanced AI also wins when it is playing against intermediate AI while advanced AI is starting the game. On this simulation advanced AI can see maximum depth at round 21 and outcome of the game at round 15. Again there are few round where advanced AI is not playing perfectly but that is enough to reach victory against intermediate AI.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/simulation_advanced30_vs_intermediate7.png" width="500">

#### Conclusions

Judging by the results, advanced AI can beat the intermediate AI (as expected) in all scenarios. It can reach the better search depth and therefore find the optimal moves to win game earlier. It is still important to keep in mind and the advanced AI is not even close to be able to play perfectly. My personal findings, while working with this project, is that most critical moves will be made within the rounds between 6 and 15. During these rounds, very good opponent, can create a situations which will lead to victory at very late game no matter if the AI is playing perfectly from the mid-game till the end. My earliest advanced AI could reach almost similar depths than the current advanced AI without heuristics, but it made very bad choices during the early game. During that time intermediate AI with search depth 7 was able to beat it on both simulations. I was also able to beat the early advanced AI as long as was able to play decent early game and avoid mistakes till the end.

Intermediate and advanced AI's are running with little bit different heuristic functions so the search depth is not only thing the measure superiority. As matter of fact, intermediate AI has more detailed heuristic and therefore it can beat the advanced AI with lower search depth as long as advanced AI timelimit will be significantly reduced.

As mentioned above, the current advanced AI is always playing non-optimal at least during few rounds. This may sound like it is not a big deal, but there is actually big impact while playing against the perfect opponent. As for example, while advanced player starts the game against perfect opponent, it will create it's first mistake at round 7. During that round, it can see up to round 28 which is nowhere enough because the winning move will be made at round 41 against two optimal players. Therefore in order to improve advanced AI to beat optimal player, would require increment of search depth by 13.

## System testing

System testing has been carried out manually.

### Installation and configuration

Software has been uploaded and tested according to [User instructions](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/instructions.md) in Linux environment.

### Functionalities

Game functionalities has been manually tested by playing the game against all versions of AI, with 2 human players and making the different AI versions to play against each other. During the manual testing, screen resolution has been 1920 x 1080. No flaws with UI transitions and key presses has been found during the manual testing. However, currently it is not implemented possibility to end the game while two AI's are playing against each other before game has ended.
