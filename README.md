# CS 11 MP
 Repository for the MP

Welcome to 3-ris!
To run the game, simply run the source code. No external imports are needed, as all imports used in the game are built-ins.
It is highly recommended to run the code in a terminal of your choice, as this is a terminal-based game.

Upon starting the game, you are prompted with a choice of 2 gamemodes, Creative and Survival, as well as an exit choice.

To proceed, you need only enter a "1" for Creative, and "2" for Survival. Entering a "3" exits the game.

Entering either "1" or "2" brings you first to several prompts.
The first prompt asks you for the number of rows you want to have for the game. By default this is set to 12 rows.
The second prompt asks you for the number of columns you want to have for the game. By default this is set to 5 columns.
The third prompt asks you for the number of colors you want to play with. This is important as this determines the difficulty of the game.
In Creative mode, you have 3 colors by default. In Survival mode, this is increased to 7 colors.

After the prompts, you proceed to the game proper. "1" starts the game in Creative, while "2" starts the game in Survival.
An integer is randomly generated from 1 to the number of colors set, which serves as the identifier for the block you drop.
These 1x1 blocks are dropped in any of the columns in the game's grid.
When a match is made, the game gets rid of the match and continues accordingly.
Note that a block can only be dropped into a column with available space; dropping it into a full one will result in an Error.

In Creative, the game ends when you successfully fill up the game's grid. In this case, you win!
In Survival, however, filling up the game's grid makes you lose! Survive for as long as possible ^-^
