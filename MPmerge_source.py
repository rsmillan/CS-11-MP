from test_suite import test_defying1, test_defying2, test_matchmake, test_delete
import time
import os
import subprocess
import sys
import random

def clear_screen():
    """Clears the terminal screen, if any"""
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([clear_cmd])


def survival():
    """Starts survival mode of the game. 
    Continues to making the grid for survival mode.
    """
    print("Welcome to Survival mode!")
    make_grid_for_survival()
    pass


def make_grid_for_survival():
    """Asks for the desired number of rows and columns for the game. 
    This is set to 12 rows and 5 columns respectively. 
    Continues to asking for colors.
    """
    rows = input("How many rows do you want? Row count:")
    while True:
        try:
            if int(rows) >= 1:
                rows = int(rows)*3
                print(f"The number of rows has been set to {rows}.")
                break
        except Exception:
            rows = 12
            print("Invalid input. The number of rows has been set to 12.")
    time.sleep(0.5)
    columns = input("How many columns do you want? Column count:")
    while True:
        try:
            if int(columns) >= 1:
                columns = int(columns)*3
                print(f"The number of columns has been set to {columns}.")
                break
        except Exception:
            columns = 5
            print("Invalid input. The number of columns has been set to 5.")
    time.sleep(0.5)
    grid = [" "*columns,]*rows
    input_colors_for_survival(columns, grid)


def input_colors_for_survival(columns,grid):
    """Asks for the desired amount of colors for the game. 
    This is set to 7 by default. Continues to game proper.
    """
    colors_amount = input("Number of colors:")
    x = 0
    try:
        colors_amount = int(colors_amount)
        if 1 <= colors_amount <= 9:
            colors_amount = int(colors_amount)
            print(f"The number of colors has been set to {colors_amount}.")
        else:
            print("Invalid input. The number of colors has been set to 7.")
            colors_amount = 7
    except Exception:
        print("Invalid input. The number of colors has been set to 7.")
        colors_amount = 7
    time.sleep(0.5)
    input_into_grid_for_survival(colors_amount, columns, grid)


def input_into_grid_for_survival(colors_amount, columns, grid):
    """This is the game proper. 
    The game first randomizes the color of the block. 
    The user then inputs the column at which this block is dropped from.
    When the block is dropped, matchmake(x, grid) is called to check for matches.
    If no match is made, the game continues. 
    If there is, the game turns the match into empty space.
    The game continues afterwards.
    """
    x = random.randint(1, colors_amount)
    print(f"Next block:{x}")
    for row in grid:
        print("│" + row + "│")
    print("╰" + "─"*(columns) + "╯")
    while True:
        col = input("Drop in column:")
        if not col:
            print(f"Please enter an integer between 1 and {columns//3}.")
            print(f"Next block:{x}")
        else:
            try:
                col = int(col)
                if grid[1][((col-1)*3)+1] != " ":
                    print("The current column is full. Please drop into a different column.")
                    print(f"Next block:{x}")
                else:
                    if 1 <= col <= columns:
                        grid = defying_gravity(x, col-1, grid)
                        for row in grid:
                            print("│" + row + "│")
                        print("╰" + "─"*(columns) + "╯")
                        time.sleep(0.5)
                        if matchmake(x,grid):
                            grid = delete_indices(matchmake(x,grid), grid)
                            for row in grid:
                                print("│" + row + "│")
                            print("╰" + "─"*(columns) + "╯")
                            time.sleep(0.75)
                            grid = _defying_gravity(grid)
                            for row in grid:
                                print("│" + row + "│")
                            print("╰" + "─"*(columns) + "╯")
                        if " " in frozenset([col for row in grid for col in row]):
                            x = random.randint(1,colors_amount)
                            print(f"Next block:{x}")
                        else:
                            print("You Lose!")
                            break
                    else:
                        print(f"Please enter an integer between 1 and {columns//3}.")
            except Exception:
                print(f"Please enter an integer between 1 and {columns//3}.")
                continue
    sys.exit()


def creative():
    """Starts creative mode of the game. 
    Continues to making the grid for creative mode.
    """
    print("Welcome to Creative mode!")
    make_grid_for_creative()
    pass


def make_grid_for_creative():
    """Asks for the desired number of rows and columns for the game. 
    This is set to 12 rows and 5 columns respectively. 
    Continues to asking for colors."""
    rows = input("How many rows do you want? Row count:")
    while True:
        try:
            if int(rows) >= 1:
                rows = int(rows)*3
                break
        except Exception:
            rows = 12
            print("Invalid input. The number of rows has been set to 12.")
    columns = input("How many columns do you want? Column count:")
    while True:
        try:
            if int(columns) >= 1:
                columns = int(columns)*3
                break
        except Exception:
            columns = 5
            print("Invalid input. The number of columns has been set to 5.")
    grid = [" "*columns,]*rows
    input_colors_for_creative(columns, grid)


def input_colors_for_creative(columns,grid):
    """Asks for the desired amount of colors for the game. 
    This is set to 7 by default. Continues to game proper.
    """
    colors_amount = input("Number of colors:")
    x = 0
    try:
        colors_amount = int(colors_amount)
        if 1 <= colors_amount <= 9:
            colors_amount = int(colors_amount)
            x = random.randint(1,int(colors_amount))
        else:
            print("Invalid input. The number of colors has been set to 3.")
            colors_amount = 3
            x = random.randint(1,colors_amount)
    except Exception:
        print("Invalid input. The number of colors has been set to 3.")
        colors_amount = 3
    input_into_grid_for_creative(colors_amount, columns, grid)


def input_into_grid_for_creative(colors_amount, columns, grid):
    """This is the game proper. 
    The game first randomizes the color of the block. 
    The user then inputs the column at which this block is dropped from.
    When the block is dropped, matchmake(x, grid) is called to check for matches.
    If no match is made, the game continues. 
    If there is, the game turns the match into empty space.
    The game continues afterwards.
    """
    x = random.randint(1, colors_amount)
    print(f"Next block:{x}")
    for row in grid:
        print("│" + row + "│")
    print("╰" + "─"*(columns) + "╯")
    while True:
        col = input("Drop in column:")
        if not col:
            print(f"Please enter an integer between 1 and {columns//3}.")
            print(f"Next block:{x}")
        else:
            try:
                col = int(col)
                if grid[1][((col-1)*3)+1] != " ":
                    print("The current column is full. Please drop into a different column.")
                    print(f"Next block:{x}")
                else:
                    if 1 <= col <= columns:
                        grid = defying_gravity(x, col-1, grid)
                        for row in grid:
                            print("│" + row + "│")
                        print("╰" + "─"*(columns) + "╯")
                        time.sleep(0.5)
                        if matchmake(x,grid):
                            grid = delete_indices(matchmake(x,grid), grid)
                            for row in grid:
                                print("│" + row + "│")
                            print("╰" + "─"*(columns) + "╯")
                            time.sleep(0.75)
                            grid = _defying_gravity(grid)
                            for row in grid:
                                print("│" + row + "│")
                            print("╰" + "─"*(columns) + "╯")
                        if " " in frozenset([col for row in grid for col in row]):
                            x = random.randint(1,colors_amount)
                            print(f"Next block:{x}")
                        else:
                            print("You Win!")
                            break
                    else:
                        print(f"please enter an integer between 1 and {columns//3}.")
            except Exception:
                print(f"PLease enter an integer between 1 and {columns//3}.")
                continue
    sys.exit()


def defying_gravity(block_num, col, g):
    """This function handles the 'drop' part of the game, 
    specifically when a block is inputted successfully.
    """
    g = list(g)
    x = len(g)
    y = len(g[0])
    g[0] = g[0][0:col*3] + "╭─╮" + g[0][col*3+3:]
    g[1] = g[1][0:col*3] + f"│{block_num}│" + g[1][col*3+3:]
    g[2] = g[2][0:col*3] + "╰─╯" + g[2][col*3+3:]
    
    def fall(g):
        if not g:
            return ()
        else:
            return list(''.join(entry) for entry in tp(_fall(g,0)))
    def _fall(g,i):
        dc_g = tuple(m for r in g for m in tuple(r)) 
        f_g = tuple(range(i,len(dc_g),len(g[0]))) 
        ran_fg = range(len(f_g))
        k_col = tuple(dc_g[f_g[k]] for k in ran_fg if dc_g[f_g[k]] == " ")
        p_col = tuple(dc_g[f_g[p]] for p in ran_fg if dc_g[f_g[p]] != " ")
        col_i = (k_col + p_col,)
        if i != len(g[0])-1:
            return (col_i) + _fall(g,i+1)
        else:
            return (col_i)
    def tp(g):
        return tuple(tuple(g[i][j] for i in range(len(g))) for j in range(len(g[0])))
    
    return fall(g)


def _defying_gravity(g):
    """This function handles the 'drop' part of the game, 
    specifically after a match is made and deleted.
    """
    g = list(g)
    x = len(g)
    y = len(g[0])
    
    def fall(g):
        if not g:
            return ()
        else:
            return list(''.join(entry) for entry in tp(_fall(g,0)))
    def _fall(g,i):
        dc_g = tuple(m for r in g for m in tuple(r)) 
        f_g = tuple(range(i,len(dc_g),len(g[0]))) 
        ran_fg = range(len(f_g))
        k_col = tuple(dc_g[f_g[k]] for k in ran_fg if dc_g[f_g[k]] == " ")
        p_col = tuple(dc_g[f_g[p]] for p in ran_fg if dc_g[f_g[p]] != " ")
        col_i = (k_col + p_col,)
        if i != len(g[0])-1:
            return (col_i) + _fall(g,i+1)
        else:
            return (col_i)
    def tp(g):
        return tuple(tuple(g[i][j] for i in range(len(g))) for j in range(len(g[0])))
    
    return fall(g)


def matchmake(x, grid):
    """Collects all instances of the grid where a 3-in-a-row, 
    3-in-a-column, or 3-in-a-diagonal have the same entries 
    and are the same with the given input.
    """
    indices_to_delete = set()
    rows = range(1, len(grid), 3)
    columns = range(1, len(grid[0]), 3)
    for row in rows:
        for column in columns:
            try: #A 3-in-a-row match is made.
                if grid[row][column] == grid[row][column+3] == grid[row][column+6] == str(x):
                    indices_to_delete.add((row,column))
                    indices_to_delete.add((row,column+3))
                    indices_to_delete.add((row,column+6))
            except Exception:
                continue
            try: #A 3-in-a-column match is made.
                if grid[row][column] == grid[row+3][column] == grid[row+6][column] == str(x):
                    indices_to_delete.add((row,column))
                    indices_to_delete.add((row+3,column))
                    indices_to_delete.add((row+6,column))
            except Exception:
                continue
            try: #A 3-in-a-diagonal match is made, which is of a descending diagonal.
                if grid[row][column] == grid[row+3][column+3] == grid[row+6][column+6] == str(x):
                    indices_to_delete.add((row,column))
                    indices_to_delete.add((row+3,column+3))
                    indices_to_delete.add((row+6,column+6))
            except Exception:
                continue
            try: #A 3-in-a-diagonal match is made, which is of an ascending diagonal.
                if grid[row][column+6] == grid[row+3][column+3] == grid[row+6][column] == str(x):
                    indices_to_delete.add((row,column+6))
                    indices_to_delete.add((row+3,column+3))
                    indices_to_delete.add((row+6,column))
            except Exception:
                continue
    return indices_to_delete


def delete_indices(indices_to_delete, grid):
    """Takes the output of matchmake(x, grid) and deletes, 
    in a similar fashion to a king piece in chess, 
    the blocks involved in the match.
    """
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)]
    if not indices_to_delete:
        return grid
    else:
        time.sleep(0.5)
        for (x,y) in indices_to_delete:
            for (x_dir,y_dir) in directions:
                grid[x+x_dir] = grid[x+x_dir][0:y+y_dir] + " " + grid[x+x_dir][y+y_dir+1:]
        return grid


def game_start():
    """Starts the program."""
    print("Welcome to 3-ris!")
    gamemode = input("What gamemode would you like to play? Enter \"1\" for Creative, \"2\" for Survival, \"3\" to exit.")
    if int(gamemode) == 1:
        print(f"Entering Creative Mode!")
        time.sleep(0.75)
        creative()
    elif int(gamemode) == 2:
        print(f"Entering Survival Mode!")
        time.sleep(0.75)
        survival()
    elif int(gamemode) == 3:
        print(f"See you next time!")
        sys.exit()
    else:
        print("Invalid input.")
        game_start()

game_start()
