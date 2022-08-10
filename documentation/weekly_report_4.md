# Weekly report 4

### What I have done during this week?

On sunday, I started working with the move exploration ordering. I did prelimary ordering for the advanced AI (basic and intermediate are not using iterative deepening method) and created simulation file in order to if the performance get's better or worse. That is still incomplete and I wasn't able to try out the differences between the old and new ordering.

On monday, I continued working with the move ordering and simulations. It is still hard to say if the move ordering is working as intended though. According to the simulations, it looks like that iterative move ordering works slightly faster than the previous ordering, which started from the closest to the middle column and ended to the columns which are closest to sides. However, at the early game state, it looks to be slightly slower (which at least partially makes sense, because the middle column is usually where the first coins should be placed). I also continued working with the bitboard presentation. The next goal is to finish bitboard presentation and test if I can improve the algorithms performance by using it instead of list matrix. After adding quite a lot new stuff, I am lacking behind with the tests and docstring, so I have to also spare some time on them before moving too much forward.

On tuesday, I yet again continued working with the bitboards. I decided to create a new entity class called position, which keeps track of game situations using the bitboard presentation. I can now run the advanced AI using bitboard presentation without errors, but there is something wrong with the implementation because the output is not as expected. I will still continue working with that, but I really need to get it working during this week or otherwise I have to reroll back to the list matrix presentation.

On wednesday I gave myself time until end of the day to get bitboards working as intended. There were plenty of bugs and I was about to give up many times, but luckily I managed to get it working. Iterative deepening can now reach up to depth between 12-13 at the early game stage with 5 second timeout, which is quite an improvement for the list matrix presentation, where I was able to reach depths between 8-9. However, algorithm only values terminal situations which means that the AI does not perform very well at the early game play. I think that even with optimisations this can be quite an issue, because with the ideal gameplay, terminal events should be happening at the very late game state. Anyway, the optimisations can wait some time because again, I am little bit behind with the tests, docstring and documentation, so these should be next things to do during this week.

### How has the program progressed?

To be added.

### What did I learn this week?

To be added.

### What was unclear or caused difficulties?

To be added.

### What do I do next?

To be added.


