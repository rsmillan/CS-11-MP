import random
import sys
import time

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
    """This function handles the 'drop' part of the game, specifically after a match is made and the blocks involved in the match have been deleted."""
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

def test_defying1():
    assert defying_gravity(1, 0, [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",]
    assert not defying_gravity(1, 0, [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "]
    assert not defying_gravity(2, 1, [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "   ╭─╮   ",
        "   │2│   ",
        "   ╰─╯   ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "]
    assert not defying_gravity(3, 2, [
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "      ╭─╮",
        "      │3│",
        "      ╰─╯",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "]
    assert not defying_gravity(2, 0, [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│2│      ",
        "╰─╯      ",
        "         ",
        "         ",
        "         "]
    assert not defying_gravity(4, 0, [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│2│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│3│      ",
        "╰─╯      "
    ]) == [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│2│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│3│      ",
        "╰─╯      "]
    assert not defying_gravity(5, 1, [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "   ╭─╮   ",
        "   │5│   ",
        "   ╰─╯   ",
        "         ",
        "         ",
        "         "]
    assert not defying_gravity(6, 1, [
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
    ]) == [
        "   ╭─╮",
        "   │6│",
        "   ╰─╯",
        "      ",
        "      ",
        "      "]
    assert not defying_gravity(7, 2, [
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
    ]) == [
        "     ╭─╮",
        "     │7│",
        "     ╰─╯",
        "      ",
        "      ",
        "      "]
    assert not defying_gravity(8, 2, [
        "      ╭─╮",
        "      │3│",
        "      ╰─╯",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == [
        "      ╭─╮",
        "      │3│",
        "      ╰─╯",
        "      ╭─╮",
        "      │8│",
        "      ╰─╯",
        "         ",
        "         ",
        "         "]
    assert not defying_gravity(9, 0, [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│2│      ",
        "╰─╯      ",
        "         ",
        "         ",
        "         "
    ]) == [
        "╭─╮      ",
        "│1│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│2│      ",
        "╰─╯      ",
        "╭─╮      ",
        "│9│      ",
        "╰─╯      "]

def test_defying2():
    assert _defying_gravity([
        "   ",
        "   ",
        " x "
    ]) == ["   ", "   ", " x "]
    assert _defying_gravity([
        "   ",
        " x ",
        "   "
    ]) == ["   ", "   ", " x "]
    assert _defying_gravity([
        "   ",
        " x ",
        " x "
    ]) == ["   ", " x ", " x "]
    assert _defying_gravity([
        " x ",
        " x ",
        " x "
    ]) == [" x ", " x ", " x "]
    assert _defying_gravity([
        "   ",
        "   ",
        "   "
    ]) == ["   ", "   ", "   "]
    assert _defying_gravity([
        "   ",
        "xx ",
        " x "
    ]) == ["   ", " x ", "xx "]
    assert _defying_gravity([
        "xxx",
        "xxx",
        "xxx"
    ]) == ["xxx", "xxx", "xxx"]
    assert _defying_gravity([
        "x  ",
        "   ",
        "   "
    ]) == ["   ", "   ", "x  "]
    assert _defying_gravity([
        "   ",
        "  x",
        "   "
    ]) == ["   ", "   ", "  x"]
    assert _defying_gravity([
        " x ",
        "x x",
        " x "
    ]) == ["   ", " x ", "xxx"]
    assert not _defying_gravity([
        "   ",
        "   ",
        " x "
    ]) == ["   ", " x ", "   "]
    assert not _defying_gravity([
        "   ",
        " x ",
        "   "
    ]) == [" x ", "   ", "   "]
    assert not _defying_gravity([
        "   ",
        " x ",
        " x "
    ]) == ["xx ", "   ", "   "]
    assert not _defying_gravity([
        " x ",
        " x ",
        " x "
    ]) == ["xxx", "   ", "   "]
    assert not _defying_gravity([
        "   ",
        "   ",
        "   "
    ]) == [" x ", " x ", " x "]
    assert not _defying_gravity([
        "   ",
        "xx ",
        " x "
    ]) == ["xx ", " x ", "   "]
    assert not _defying_gravity([
        "xxx",
        "xxx",
        "xxx"
    ]) == ["   ", "   ", "   "]
    assert not _defying_gravity([
        "x  ",
        "   ",
        "   "
    ]) == ["x  ", "x  ", "   "]
    assert not _defying_gravity([
        "   ",
        "   ",
        "  x"
    ]) == ["  x", "   ", "   "]
    assert not _defying_gravity([
        " x ",
        "x x",
        " x "
    ]) == [" x ", " x ", " x "]

def matchmake(x, grid):
    """Collects all instances of the grid where a 3-in-a-row, 3-in-a-column, or 3-in-a-diagonal have the same entries and are the same with the given input."""
    indices_to_delete = set()
    rows = range(1, len(grid), 3)
    columns = range(1, len(grid[0]), 3)
    for row in rows:
        for column in columns:
            try: #3-in-a-row
                if grid[row][column] == grid[row][column+3] == grid[row][column+6] == str(x):
                    indices_to_delete.add((row,column))
                    indices_to_delete.add((row,column+3))
                    indices_to_delete.add((row,column+6))
            except:
                continue
            try:
                if grid[row][column] == grid[row+3][column] == grid[row+6][column] == str(x):
                    indices_to_delete.add((row,column))
                    indices_to_delete.add((row+3,column))
                    indices_to_delete.add((row+6,column))
            except:
                continue
            try:
                if grid[row][column] == grid[row+3][column+3] == grid[row+6][column+6] == str(x):
                    indices_to_delete.add((row,column))
                    indices_to_delete.add((row+3,column+3))
                    indices_to_delete.add((row+6,column+6))
            except:
                continue
            try:
                if grid[row][column+6] == grid[row+3][column+3] == grid[row+6][column] == str(x):
                    indices_to_delete.add((row,column+6))
                    indices_to_delete.add((row+3,column+3))
                    indices_to_delete.add((row+6,column))
            except:
                continue
    return indices_to_delete

def test_matchmake():
    assert matchmake(1, [
        "         ",
        " 1  1  1 ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == {(1, 1), (1, 4), (1, 7)}
    assert matchmake(2, [
        "         ",
        " 2       ",
        "         ",
        "         ",
        " 2       ",
        "         ",
        "         ",
        " 2       ",
        "         "
    ]) == {(1, 1), (4, 1), (7, 1)}
    assert matchmake(3, [
        "         ",
        " 3       ",
        "         ",
        "         ",
        "    3    ",
        "         ",
        "         ",
        "       3 ",
        "         "
    ]) == {(1, 1), (4, 4), (7, 7)}
    assert matchmake(4, [
        "         ",
        "       4 ",
        "         ",
        "         ",
        "    4    ",
        "         ",
        "         ",
        " 4       ",
        "         "
    ]) == {(1, 7), (4, 4), (7, 1)}
    assert matchmake(5, [
        "         ",
        " 5  5  5 ",
        "         ",
        "         ",
        " 5       ",
        "         ",
        "         ",
        " 5       ",
        "         "
    ]) == {(1, 1), (1, 4), (1, 7), (1, 1), (4, 1), (7, 1)}
    assert not matchmake(1, [
        "         ",
        " 1       ",
        "         ",
        " 1       ",
        "         ",
        " 1       ",
        "         ",
        "         ",
        "         "
    ]) == {(1, 1), (4, 1), (7, 1)}
    assert not matchmake(2, [
        "         ",
        " 2 2 2   ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         ",
        "         "
    ]) == {(1, 1), (1, 4), (1, 6)}
    assert not matchmake(3, [
        "         ",
        " 3       ",
        "         ",
        " 3       ",
        "         ",
        " 3       ",
        "         ",
        "         ",
        "         "
    ]) == {(1, 1), (1, 4), (1, 7)}
    assert not matchmake(4, [
        "         ",
        " 4       ",
        "         ",
        "   4     ",
        "         ",
        "     4   ",
        "         ",
        "         ",
        "         "
    ]) == {(1, 1), (4, 2), (7, 7)}
    assert not matchmake(5, [
        "         ",
        "       5 ",
        "         ",
        "     5   ",
        "         ",
        "   5     ",
        "         ",
        "         ",
        "         "
    ]) == {(1, 4), (1, 5), (1, 6)}

def delete_indices(indices_to_delete, grid):
    """Takes the output of matchmake(x, grid) and deletes, in a similar fashion to a king piece in chess, the blocks involved in the match."""
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)]
    if not indices_to_delete:
        return grid
    else:
        time.sleep(0.5)
        for (x,y) in indices_to_delete:
            for (x_dir,y_dir) in directions:
                grid[x+x_dir] = grid[x+x_dir][0:y+y_dir] + " " + grid[x+x_dir][y+y_dir+1:]
        return grid

def test_delete():
    grid = [
        "`````````",
        "`1``1``1`",
        "`````````",
        "`````````",
        "`````````",
        "`````````",
        "`````````",
        "`````````",
        "`````````"]
    indices_to_delete = matchmake(1, grid)
    assert indices_to_delete == {(1, 1), (1, 4), (1, 7)}
    new_grid = delete_indices(indices_to_delete, grid)
    assert new_grid == [
        "         ",
        "         ",
        "         ",
        "`````````",
        "`````````",
        "`````````",
        "`````````",
        "`````````",
        "`````````"]
    grid = [
        "`````````",
        "`5``5``5`",
        "`````````",
        "`````````",
        "`5```````",
        "`````````",
        "`````````",
        "`5```````",
        "`````````"
    ]
    indices_to_delete = matchmake(5, grid)
    assert indices_to_delete == {(1, 1), (1, 4), (1, 7), (4, 1), (7, 1)}
    new_grid = delete_indices(indices_to_delete, grid)
    assert new_grid == [
        "         ",
        "         ",
        "         ",
        "   ``````",
        "   ``````",
        "   ``````",
        "   ``````",
        "   ``````",
        "   ``````"
    ]
    grid = [
        "`````````",
        "`3` ` ` `",
        "`````````",
        "` `3` ` `",
        "`````````",
        "` ` `3` `",
        "`````````",
        "`````````",
        "`````````"
    ]
    indices_to_delete = matchmake(3, grid)
    assert not indices_to_delete == {(1, 1), (4, 3), (7, 7)}
    new_grid = delete_indices(indices_to_delete, grid)
    assert not new_grid == [
        "`````````",
        "`3` ` ` `",
        "`````````",
        "` ` ` ` `",
        "`````````",
        "` ` ` ` `",
        "`````````",
        "`````````",
        "`````````"
    ]
    grid = [
        "`````````",
        "`5`5`5` `",
        "`````````",
        "`5` ` ` `",
        "`````````",
        "`5` ` ` `",
        "`````````",
        "`5` ` ` `",
        "`````````"
    ]
    indices_to_delete = matchmake(5, grid)
    assert not indices_to_delete == {(1, 1), (1, 4), (1, 7), (1, 1), (7, 1)}
    new_grid = delete_indices(indices_to_delete, grid)
    assert not new_grid == [
        "       ``",
        "       ``",
        "       ``",
        "   ``````",
        "   ``````",
        "   ``````",
        "   ``````",
        "   ``````",
        "   ``````"
    ]

test_defying1()
test_defying2()
test_matchmake()
test_delete()