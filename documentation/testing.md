# Testing document

## Test coverage report

Coverage report can be generated using the command:

```
poetry run invoke coverage-report
```

Report will be generated into the folder named `htmlcov`. Coverage report can be also found from the [Codecov](https://app.codecov.io/gh/TopiasHarjunpaa/C4AI).

Following files are left out from the coverage report:
* UI -files
* testing -files
* configuration-, simulation- and index file

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/coverage_report.png" width="1000">

Methods which were not tested: 
* Trivial methods, such as Getters, Setters and few pygame event key checks
* Printing methods
* AI move calculations methods in `GameService` class which are already tested in `AiService` class.

## Unit and integration testing

### Entities classes

Most of the `Entities` class testing has been made at the integration test level. There are few tests made for the [TestSprites](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/entities/sprites_test.py) class which tests initialization of game board, drawing new coins and adding them to the corresponding sprite groups.

*Note. These tests could be considered trivial ones and perhaps test wouldn't be necessary. However, at the earlier stage of the project, these were invented in a different way and I decided to keep these tests instead of deleting them*

### Service classes

The following test classes has been made to test service classes:

1.  [TestAiService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/ai_service_test.py)

    Description to be added

2.  [BitboardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/bitboard_service_test.py)

    Description to be added

3.  [TestBoardService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/board_service_test.py)

    Description to be added

4.  [TestGameService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/game_service_test.py)

    Description to be added

    Stub classes used:

    * `StubClock`
    * `StubEventQueue`
    * `StubRenderer`
    * `StubAudio`
    * `StubUI`

    `GameService` class uses stub class functions which are unnecessary from the testing perspective.

5.  [TestHeuristicService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/heuristic_service_test.py)

    Description to be added

6.  [TestSituationService](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/services/situation_service_test.py)

    Description to be added

Many service classes has multiple methods which keeps track of the game situation. In order to test different game situation, [test_grids.py](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/test_grids.py) and [test_locs.py](https://github.com/TopiasHarjunpaa/C4AI/blob/main/src/tests/test_locs.py) has been created. Test grids obviously contains different game grid setups and Test locs contain different setups for Four Connect testing.

## System testing

System testing has been carried out manually.

### Installation and configuration

To be added.

### Functionalities

To be added.

## Performance testing

To be added.