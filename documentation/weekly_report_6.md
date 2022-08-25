# Weekly report 6

### What I have done during this week?

On Sunday I continued working with documentation. Primarily for the implementation documents. Meanwhile I also did some minor refactoring in order to keep project structure as mentioned at the implementation document.

On monday I continued working with documentation. I created user instruction document which still needs updated link for the final release. I also updated implementation and testing documents which both are close to finished. For the implementation document I perhaps may add a class diagram and list of improvement ideas. For the testing document I may add few words about simulation file but that file actually would need some reworking. Another option would be just to remove whole file entirely as it was made for comparing old implementations.

On tuesday I only did peer reviewing. It took quite some time but it was nice experience especially because the subject wasn't familiar to me.

On wednesday I tried to investigate new optimisation possibilities, but did not implement anything. Instead of that, I spend few moments for renaming the variable names and some methods according to the comments from the peer review.

On thursday I tested different transposition table solutions and compared the results by simulating the first 12 rounds of the game:
- Firstly I compared current transposition table against no transposition table at all. Current transposition table reached depths between 17-21 while no transposition table reached depths between 15-17.
- Secondly I compared current transposition table against ordered transposition table and size limit of 100000 entries. The results were again worse than the current implementation. Little bit better than no transposition table at all.
- Thirdly I compared current transposition table against ordered transposition table and size limit of 500000 entries. The results were again worse, but quite close to current implementation. However the current implementations holds slighlty more than 600000 entries so the difference wasn't that big.
After these tests I came in the conclusion that I will keep the original and probably are not going to optimise that anymore. I ended up however tuning little bit heuristic values which seemed to give minor speed up for the algorithm after round 8 and onwards while being little bit slower before the round 8. Most of the time I spend with reworking the simulation and plotting the search depth results. Currently there is possibility to simulate three different game scenarios:
- Intermediate AI vs. advanced AI
- Advanced AI vs. intermediate AI
- Advanced AI vs. advanced AI
The results were pretty much as expected. Advanced AI beats the intermediate AI in all scenarios and it can reach maximum depth at rounds between 15 and 20. Next plan is to analyze these results at the testing documentation.

### How has the program progressed?

To be added.

### What did I learn this week?

To be added.

### What was unclear or caused difficulties?

To be added.

### What do I do next?

To be added.