# Weekly report 2

### What I have done during this week?

On sunday, I created setup view which allows user to change different player setups such as player vs. player or player vs. AI etc. I also created preliminary AI (chooses game coin locations randomly) and adjusted game loop logic so that AI development can be started.

On monday, I did spent most of the time for creating unit and integration tests. I also created preliminary base for the ai service class and for its tests. On top of that, I did some small refactoring for the UI classes.

On tuesday, I created preliminary heuristic value calculation for game scenarios. This also involved quite a lot changes for the existing code and for that reason I spent most of the time modificating the code structure and tests.

Wednesday will be my last working day for the project before week 2 deadline. I did continue working with heuristic value calculations and I also created minimax algorithm with alpha-beta pruning. After playing the game few times, I am quite confident that the AI is playing better than it did when I played the game only with heuristic value calculation. However, I am almost as confident that there are still some flaws with the algorithm or the heuristic value calculations, because it didn't that hard to defeat using the search depth of 6.

### How has the program progressed?

From previous week, I had planned to implement Minimax algorithm, create setup view for the UI (in order to change play modes) and create two levels for the algorithm to measure the differences. From these goals, I managed to do all but the last one. However, I think that can be implemented within very short of time when needed.

### What did I learn this week?

On this week, I needed to make multiple changes for the classes and methods. Even though I did not have very comprehensive test coverage, I found out how useful these automated tests actually are. Even in a small project like this, I felt like saving lot's of time without needing to manually test the modifications made for the code base.

Last week I also wrote about the concerns how to actually apply Minimax algorithm to the Connect Four -game. During this week, at least those concerns has been vanished, so guess I can say that I have also learned something about Minimax algorithm and how to implement it in general. However, I do know that there are still lot's of things to learn in order to get good understanding of that.

### What was unclear or caused difficulties?

I still have plenty of uncertainties related to the heurestic calculations at Connect Four -game. So far, I have just applied almost random values for certain game scenarious. I found a research article [Research on Different Heuristics for Minimax Algorithm Insight from Connect-4 Game](https://www.researchgate.net/publication/331552609_Research_on_Different_Heuristics_for_Minimax_Algorithm_Insight_from_Connect-4_Game) which may give me some ideas how to improve the heurestics.

Other than that, I did not have any specific difficulties. I did have some problems in general level at the code writing, mostly because it's been already sometime since I last time coded with Python. There are currently some quite ugly code which I have to refactor at in coming weeks. One to mention, there are currently grid matrix initialized using the list comprehension and I spend too much time for figuring out why I can not create proper copy of that matrix without altering the original matrix. For that I ended up creating temporary solution which needs to be fixed.

### What do I do next?

Due lack of time for this week, I am still lacking most of the tests for the AI class. I do also have some concerns that there may be quite some things to modificate in order to improve AI gaming abilities. That being said, I will mostly focus on creating unit and integration test and probably fixing the bugs which will be discovered during the testing process. I will also start writing the testing documentation.