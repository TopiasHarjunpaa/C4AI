# Weekly report 4

### What I have done during this week?

On sunday, I started working with the move exploration ordering. I did prelimary ordering for the advanced AI (basic and intermediate are not using iterative deepening method) and created simulation file in order to if the performance get's better or worse. That is still incomplete and I wasn't able to try out the differences between the old and new ordering.

On monday, I continued working with the move ordering and simulations. It is still hard to say if the move ordering is working as intended though. According to the simulations, it looks like that iterative move ordering works slightly faster than the previous ordering, which started from the closest to the middle column and ended to the columns which are closest to sides. However, at the early game state, it looks to be slightly slower (which at least partially makes sense, because the middle column is usually where the first coins should be placed). I also continued working with the bitboard presentation. The next goal is to finish bitboard presentation and test if I can improve the algorithms performance by using it instead of list matrix. After adding quite a lot new stuff, I am lacking behind with the tests and docstring, so I have to also spare some time on them before moving too much forward.

On tuesday, I yet again continued working with the bitboards. I decided to create a new entity class called position, which keeps track of game situations using the bitboard presentation. I can now run the advanced AI using bitboard presentation without errors, but there is something wrong with the implementation because the output is not as expected. I will still continue working with that, but I really need to get it working during this week or otherwise I have to reroll back to the list matrix presentation.

On wednesday I gave myself time until end of the day to get bitboards working as intended. There were plenty of bugs and I was about to give up many times, but luckily I managed to get it working. Iterative deepening can now reach up to depth between 12-13 at the early game stage with 5 second timeout, which is quite an improvement for the list matrix presentation, where I was able to reach depths between 8-9. However, algorithm only values terminal situations which means that the AI does not perform very well at the early game play. I think that even with optimisations this can be quite an issue, because with the ideal gameplay, terminal events should be happening at the very late game state. Anyway, the optimisations can wait some time because again, I am little bit behind with the tests, docstring and documentation, so these should be next things to do during this week.

Yesterday I ended up creating very brief test code for transposition table and today on thursday I created very quickly own class for that. It clearly does not work as it should be right now, but I decided to keep it, so I continue from that if needed. Most of the time today I spend for creating new tests, playing around with the simulations and did couple of test matches against the advanced AI. Judging by the game results, the advanced AI is not quite ready yet.

On Friday I spend most of the time just playing around with the current model and tried to create optimisations without much of an improvements. I tried for example different heuristics and move ordering, but the problem most likely was that those tests were quite hastily made and probably weren't implemented properly. I need to focus on these optimisations more carefully at next week.

On saturday I just refactored and formated code base and spend remaining time on the documentation.

### How has the program progressed?

My last week goal was to create working bitboard presentation which I managed to do. Besides documentation that was unfortunately only solid thing I managed to do on this week. I did try out many other optimisations, but I did not manage to get those work. In general this week was little bit frustrating because my expectations for the improvements were higher. However I am trying to motivate myself that I still have a working solution which can beat myself most of the games even if it not playing perfectly.

### What did I learn this week?

I would like to say binary operations, because I spend most of the time for the bitboard presentation. Although the current operations used on this project are mostly just taken from the pseudocode examples with small modifications. Anyway I at least can know understand the very basics of them.

This was also first week on this project where things did not progress very smoothly so I needed to learn patience that everything can not always go as smoothly and expected. On this week I had some days where I changed a lot at the code base and after end of the day I needed to roll back most of the implementations.

### What was unclear or caused difficulties?

After I managed to create bitboard presentation with terminal situation heuristics, I quite soon realised that algorithm does not play early game very well. I understand that increasing the search depth will make it better, but I still have to figure out a way how to make algorithm prevent opponents early moves which will be realised for opponents victory at the very end of the game. The current algorithm can see the outcome of the game at the turns between 15-20. Problem on that is that the opponent can create game situation within 15 first moves which will lead into victory (if not making bad mistakes) at very late game.

### What do I do next?

Next week I am trying to solve this early game problem for the algorithm. There are several things I have planned to try out. I am not right not super confident that I will be to create a massive boost for the algorithm and right now I am happy if I can make it even tiny bit better. Some to mention I will try to create:

- better move exploration ordering
- use of transposition table
- early game heuristics if needed to make the first two work properly
- check if the board has symmetrical situation to narrow down search path


