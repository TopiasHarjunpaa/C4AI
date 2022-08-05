# Weekly report 3

### What I have done during this week?

On sunday, after extended weekend break from the project, I mainly re-wrote and added new docstring and improved testing coverage. I also did some minor changes for some methods, such as renaming and re-ordering their structures.

On monday, I continued updating the docstring and did most of the unit tests for the current services. There are still some tests missing especially for the game services. I also added possibility to run two different levels of AI algorithms and checkings for the situation when game has ended in draw. On top of that, did some improvements for the UI, suchs as background image and logos. I know that it is not best way to spend time as it is not the primary scope for this project. However, I still have to run the software plenty of times and I'd like that it looks just little bit better. This being said, I still may update the game board and game coins looks, which should not take too much time.

On tuesday, I started creating some improvements for the UI such as drawing game board and coins. I expected that to be quick job to implement, but suddenly I realised spending almost whole evening for doing that. I am still not satisfied for the looks of the UI, but I decided to not spend more time on that as long as there are work left to do with the algorithms. Perhaps at the end of the project I may do some minor tuning if I have time left.

On wednesday I started finally implementing new stuff for the AI. I had studied earlier some methods to optimise Minimax algorithms and decided to give a go for iterative deepening. I think I managed to somehow do that, but I need to take a further look for that tomorrow and implement tests as well. I also managed to break one test for the game loop services which needs to be fixed.

Thursday was little bit lazy day in terms of project work. During the day I occasionally tried to read from the internet some new information related to the improvements of the AI algorithms. Mostly related to the bitboard presentation and transposition tables. I did not start yet implementing those since there are still some uncertainties which I want to discover first. However, I did minor improvement for the AI by changing the order how the available locations will be looped inside the Minimax algorithm. Instead starting from first available column from the left, I decided to start from the closest to the middle column and end to the closest columns at the sides. Reasons for this change was that, at least in the early stages, the optimal moves are more likely to be found at the middle. With this change, I was able to increase search depth from 6 up to 9 which took roughly 7-8 seconds at the early stage. However, I did not test what will happen after few starting rounds.

My main goal for Friday was to create prelimary testing document. Aside from that I did study bitboard presentation from Dominikus Herzbergs [Bitboards and Connect Four document](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md) and after reading it couple of times, I decided to give it ago. I did very brief implementation and tests to check winning situation and judging by the results that seems to be working. I am still struggling to figure out proper way how to get most out of that, as full implementation at least, would require massive changes for the current classes. On other hand, I would like to keep current matrix presentation available for the comparing purposes.

### How has the program progressed?

To be added

### What did I learn this week?

To be added

### What was unclear or caused difficulties?

To be added

### What do I do next?

To be added