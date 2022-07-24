# Project definition
**Study degree: University of Helsinki: Bachelor's Programme in Computer Science**  
**Project documentation language: English**  
**Programming language: Python**  

The main goal for the C4AI project is to create AI which plays Connect Four computer game against the player and possibly against different level AI's as well. 

The game will have a simple graphical UI with main menu, setup and playing mode. In main menu, user can select starting a new game or go to setup and select opponent type (player, easy AI, moderate AI, hard AI etc.) On top of that, user can choose to run different simulations from the command line, such as performance tests and comparisons between different AI's.

Matrix with size of 6 rows and 7 columns will be initialised with zeros (int) at the start of the game. For each round, player will choose the column to drop the game coin. Input will be integer between the 0 - 6 which indicates the indexes of the column. Row index will be bottom-most free slot on the chosen column. According to that decision, matrix will be updated with the value of 1 or 2 depending if it's first or second player turn. Using that matrix, the program will keep up with the game situation and checks the game ending situations (win or draw). Using the same matrix, AI will compute the next move and as a output, it returns the integer between 0 - 6 which indicates as well the indexes of the game board columns.

Projects minimum requirement is to create AI using the Minimax algorithm and Alpha-beta pruning to compete against player. Minimax algorithm seems to be common solutions to create AI algorithm for the games such as Connect Four.On top of that, there will be several ways to expand the project. One option would be to create another AI using Monte Carlo Search Tree and compare the results between AI's using the Minimax. Another option could be focus around the Minimax algorithm and try to improve it's performance using some additional methods, such as binary representation or iterative deepening. Right now, the MCST sounds more interesting aprouch, but I haven't spend much time looking for those in detail. So it is still very unclear how likely it is to implement those within the timeframe of the project.

In order to set up couple of measurable goals, I would say that the AI should spend at most 5 seconds to calculate next move. I am also expecting that it should be able to beat me in most of the games.

#### Sources:  
[Minimax (Wikipedia)](https://en.wikipedia.org/wiki/Minimax)  
[Alpha-beta pruning (Wikipedia)](https://en.wikipedia.org/wiki/Alpha_beta_pruning)  
[Solving connect 4: How to build a perfect AI](http://blog.gamesolver.org/)  

