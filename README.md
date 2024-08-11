# CS 11 MP
 Repository for the MP

**Instructions and Mechanics**
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

**The Coder's Side**
I organized the code into 5 "parts": the imports, survival, creative, fall-and-match, and game start.
Each of these parts serve a purpose to the overall MP:
- imports to import all needed builtin packages;
- survival and creative to run the 2 main gamemodes of the game;
- fall-and-match for the heart of the game, and
- game start to start the game in the first place.
I tried to implement a top-down approach as much as possible, first in my own way, then editing it to follow the PEP8 Style Guide.

The game starts, prompting the user for a gamemode or an exit. If they run a gamemode, they are then asked for game size and number of colors for the playthrough.
Then, the game proper begins. Matches are made when a match is made **and** the match's entries are the same as that of the last block dropped.
I know this is not the intended result of the matchmaking function, but I could no longer debug it.
I also did not use the clear_screen() function, as it was causing my program to bug out.

**Unit Testing**
In terms of unit testing, I tried to stay as simple as possible, going for trivial and edge cases alike but not producing so many of them at once.
You can run the file containing these tests separately, as I have placed in the file the functions I could unit test for.
Conversely, I have put these tests in the source code as an import, which should work.
To add new tests, you need only add new tests in the correct function in the unit test file, test_suite.py.

**Bonus Features**
I'd like to be credited points for the following bonus features:
1. Survival Mode
2. Custom Game Size
3. Custom Color Amount
4. "You Lose!" ending message for Survival Mode
5. Exit option at the start of the Program
