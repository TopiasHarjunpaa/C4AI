# Weekly report 5

### What I have done during this week?

Sunday was rather lazy day in terms of project work. After last week frustration, I decided to play around again with the current model yet again without improvement. I pretty much came in a conclusion (which can be very wrong) that I can not improve early game without adding better heuristic.

On monday I started working with new heuristic for the bitboards. I had already tried out this earlier without success. This time I managed to create heuristic which counts how many three connects the player has at the certain board configuration. Currently the heuristic value for 3 connects are simply calculated by: number of player 3 connects reduced by number of opponent 3 connects. On top of that I added additional 3 points for each coin placed at the middle column. This is something I need to reinvestigate if it is going to be necessary. I also created move exploration ordering which primarily ranks the move order by heuristic values recieved from the previous iterations and secondarily by the middle column ordering. Finally I recreated transposition table, but again I feel like that needs additional investigation in order to make it work properly. As a result from mondays work the algorithm is playing significantly better early game. It can now search within 5 seconds up to depth 12 in early game while it previously was able to search roughly 14 depths. It can now predict the outcome of the game roughly around round of 20 while it previously was able to find it slightly earlier.

On tuesday I created additional check for finding available columns which cuts the number of available columns if opponent can get victory during next turn ie. if player has to block certain column in order to prevent losing, it makes no sense to investigate other columns further. This allowed to reach one depth further during the early game. That was quite fast implementation and most of the time I spend for creating docstring for bitboard classes as I hadn't done that during the implementations of those classes. I also found out that current iterative deepening Minimax search probably returns too much information as it is now returning also list of all available columns and their heuristic values. This means that I probably do not need to return chosen column number and heuristic value separately. There are however other things to take care and changing this may complicate other stuff, so I am not sure I am going to change that very soon at least.

On wednesday I created checking for the symmetrical game board situations. I assumed that this will be beneficial to narrow down search paths at the early game. I also created additional boolean parameter for the AI class to keep track if the game board has evolved from the symmetrical situation to non-symmetrical situation. There may be some cases when game can actually evolve back to the symmetrical, but I assume that the time saving from not running the symmetrical checks after game has evolved to non-symmetrical will be more beneficial than consider cases where game might evolve back to symmetrical. Anyway this wasn't the game changer for the algorithm. Judging by the few tests, this reduced roughly 10 - 15% of calculation time on a last iteration at the early game. On top of that I did few additional tests for the game service class and updated testing documentation which is still quite an incomplete.

On thursday I started implementing multiprocessing first to the Minimax algorithm, but I did not manage to get it working. I also tried multiprocessing and multithreading to run looped binaryoperations which I actually managed to run without errors, but I ended up using more calculation time instead of benefiting anything. I quite quickle rolled back where I left yesterday and decided to spend time for other things. Most of the time I spend for peer reviewing and state of the actual project did not get any improvement today.

### How has the program progressed?

To be added.

### What did I learn this week?

To be added.

### What was unclear or caused difficulties?

To be added.

### What do I do next?

To be added.