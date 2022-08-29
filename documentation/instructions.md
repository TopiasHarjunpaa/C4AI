# User instructions

Download the latest [release (placeholder)](https://github.com/TopiasHarjunpaa/C4AI/releases/tag/week4)

## Assembly instructions

Install dependencies

```
$ poetry install
```

Start the program using the command:

```
$ poetry run invoke start
```

## Playing instructions

C4AI name refers to board game [Connect Four](https://en.wikipedia.org/wiki/Connect_Four). In this game, user can play against different level AI's or against other human player. Game has following views / states:

1. Main menu
2. Game setup
3. Game view
4. Game over view

### Main menu:

Main menu will be shown after game has launched. There are following options:
1. Start new game by pressing the key `N`
2. Open game settings by pressing the key `S`
4. Exit the game by pressing the key `ESC` or the closing icon at the top-right of the screen.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/C4AI_main_menu.png" width="700">

### Game setup:

In a game setup user can change the opponent type and difficulty level of the AI:
1. Each player can be chosen to be human or AI player.
2. There are total of 4 player types: Player (human), AI (basic), AI (Minimax depth 7) and AI(Minimax opt.)
3. First player can be changed by pressing the key `1`. Each key press will change the type to the next one.
4. Second player can be changed by pressing the key `2`. Each key press will change the type to the next one.
5. User can go back to the main menu by pressing the key `ESC`. Current player setup will be automatically saved.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/C4AI_setup1.png" width="700">
<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/C4AI_setup2.png" width="700">

### New game / Game view:

New game with empty game board. On top of the board text indicates which player turn it is currently. Red color means player 1 and yellow color means player 2. Column to drop game coin will be chosen by pressing the keys 1-7 which indicates the column numbers from left to right. Column numbers are indicated below the game board.

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/C4AI_game_on.png" width="700">

### Game over:

Game will end either when one of the players has won the game ie. gotten four connect or when all the game coins are used and none of the players has won ie. ended draw. Game over is indicated at the top of the board and user can choose to play again by pressing the key `N`. User can go back to main menu by pressing the key `ESC` when game is over or while it is users turn. 

<img src="https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/pictures/C4AI_game_over.png" width="700">