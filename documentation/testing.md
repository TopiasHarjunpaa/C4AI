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

## System testing

System testing has been carried out manually.

### Installation and configuration

Software has been uploaded and tested according to [User instructions](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/instructions.md) in Linux environment.

### Functionalities

Game functionalities has been manually tested by playing the game against all versions of AI, with 2 human players and making the different AI versions to play against each other. During the manual testing, screen resolution has been 1920 x 1080. No flaws with UI transitions and key presses has been found during the manual testing. However, currently it is not implemented possibility to end the game while two AI's are playing against each other before game has ended.