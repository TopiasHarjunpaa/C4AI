# Weekly report 1

### What I have done during this week?

Starting lecture was held on monday and after that I spend few hours for thinking about the proper topic. I also did some preliminary coding around certain topic I had in my mind to choose for this project.

On tuesday, I decided to change the subject for Connect Four AI algorithm and spend most of my to initialising GitHub repository and creation of walking skeleton for the project.

On wednesday and thursday I started implementing graphical game UI with pygame library along with some game rules and logic.

On friday, I managed to finish playable version of the Connect Four. There are still some minor flaws at the logic side and the UI does not have the best appearence. I also prepared Github Actions, did some Docstring and created several tests for the game logic.

On saturday, I mainly did documentation work. Also along all these days, I have spent little bit time for learning the algorithms for game AI, such as Minimax algorithm and alpha-beta pruning.

### How has the program progressed?

As said above, I have created playable version of the Connect Four game with graphical UI made by using the pygame library. There are only player vs. player option available so I haven't yet started implementing any sort of AI algorithms as for the game opponents.

### What did I learn this week?

Most of my implementations so far has been repeat of already learned tools and methods. However, it took me while (and still will take some time) to memorise how to create game using the pygame. I would say that most of the new stuff which I have learned has came from the articles and videos about the Minimax algorithm and alpha-beta pruning. Due the reason I haven't yet implemented any of them, it is still too early to say how well I have actually learned those subjects.

### What was unclear or caused difficulties?

I feel like I have general understanding how the Minimax algorithm should work, but right now I am still uncertain how to apply that algorithm specifically for the Connect Four -game. 

As I have understood, I should be able to rank different kind of game situations with the values which are used at the algorithm. I also know that there are several moves which can be worth more than other moves. But finding the proper values for different scenarious is still a bit unclear.

Secondly, right now I have no idea how to evaluate how well the actual algorithm will be working. Perhaps I can do some time measuring how long it takes to calculate move using certain depth, but I still have no clear idea how to evaluate if the AI is improving ie. being more likely to win opponents.

Thirdly, I am having problems to figure out how to do proper testing for algorithm. For example if I want to test that algorithm will find the best possible move at certain point of the game, I most likely have no idea which actually is the best possible move unless it is very clear case.

### What do I do next?

Week 2 plan is to implement Minimax algorithm. I will also create setup view for the UI where the user can choose the play modes, such as, player vs. player and player vs. AI. Ideally I should have at least two levels for the AI in order to measure the improvements of the AI.