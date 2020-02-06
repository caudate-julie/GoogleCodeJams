# April 12, 2014
# Qualification Round
# "Minesweeper Master"
# = Kyra =

from time import time

#inpath = "C-sample.in"
inpath = "C-large.in"
#inpath = 'C-small-attempt2.in'
outpath = "C.out"

timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

def RowMine(grid, mines):
    for i in range(mines):
        grid[i][0] = "*"
    grid[-1][0] = "c"
    return grid

def ColumnMine(grid, mines):
    for i in range(mines):
        grid[0][i] = "*"
    grid[0][-1] = "c"
    return grid 

def OneMine(grid):
    grid[0][0] = 'c'
    return grid

def TwoColumnMine(grid, spaces):
    for i in range(spaces / 2):
        grid[i][0] = '.'
        grid[i][1] = '.'
    grid[0][0] = 'c'
    return grid

def TwoRowMine(grid, spaces):
    for i in range(spaces / 2):
        grid[0][i] = '.'
        grid[1][i] = '.'
    grid[0][0] = 'c'
    return grid

def SquareMine(grid):
    grid[0][0] = 'c'
    grid[1][0] = '.'
    grid[0][1] = '.'
    grid[1][1] = '.'
    return grid
    
def SnakeMine(grid, space):
    for i in range(space / 2):
        grid[0][i] = '.'
        grid[1][i] = '.'
    grid[0][0] = 'c'
    return grid

def BentSnakeMine(grid, space):
    for i in range(space / 2 - 1):
        grid[0][i] = '.'
        grid[1][i] = '.'
    grid[2][0] = '.'
    grid[2][1] = '.'
    grid[2][2] = '.'
    grid[0][0] = 'c'
    return grid

def LineMine(grid, row, column, space):
    full_lines = space / column
    remain = space % column
    for i in range(full_lines):
        for j in range(column):
            grid[i][j] = '.'
    for j in range(remain):
        grid[full_lines][j] = '.'
    if remain == 1:
        grid[full_lines][1] = '.'
        grid[full_lines - 1][-1] = '*'
        if full_lines == 2:
            grid[full_lines][2] = '.'
            grid[full_lines - 2][-1] = '*'
    grid[0][0] = 'c'
    return grid
        
def MineSweeper(row, column, mines):
    grid = [["." for i in range(column)] for j in range(row)]
    if mines == 0:
        return OneMine(grid)
    if column == 1:
        return RowMine(grid, mines)
    if row == 1:
        return ColumnMine(grid, mines)
    space = row * column - mines
    for i in range(row):
        for j in range(column):
            grid[i][j] = '*'
    if space == 1:
        return OneMine(grid)
    if space < 4 or space == 5 or space == 7:
        return None
    if space == 4:
        return SquareMine(grid)
    if row == 2 and mines % 2 == 0:
        return TwoRowMine(grid, space)
    if column == 2 and mines % 2 == 0:
        return TwoColumnMine(grid, space)
    if row == 2 or column == 2:
        return None    
    if space / column < 2:
        if space % 2 == 0:
            return SnakeMine(grid, space)
        else:
            return BentSnakeMine(grid, space)
    else:
        return LineMine(grid, row, column, space)
    
T = int(fin.readline())
for case in range(1, T+1):
    R, C, M = map(int, fin.readline().split())
    grid = MineSweeper(R, C, M)
    fout.write("Case #%d:\n" % case)
    if grid == None:
        fout.write("Impossible\n")
    else:
        for r in grid:
            for c in r:
                fout.write(c)
            fout.write("\n")
    #print case
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
