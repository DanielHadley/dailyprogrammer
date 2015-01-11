######################################
# Challenge 165E: ASCII Game of Life #
#           Date: June 1, 2014       #
######################################

# Read the input.

# Hello people. Sorry for submitting this early, but I have exams this week and the next so I'll have to submit these challenges a little bit early - I'm sure that's not an issue though! Welcome to June, and it's time for a run of similarly themed challenges - all of them will be based on ASCII data. Not too dissimilar to this challenge from a while ago.
# This first challenge is based on a game (the mathematical variety - not quite as fun!) called Conway's Game of Life. This is called a cellular automaton. This means it is based on a 'playing field' of sorts, made up of lots of little cells or spaces. For Conway's game of life, the grid is square - but other shapes like hexagonal ones could potentially exist too. Each cell can have a value - in this case, on or off - and for each 'iteration' or loop of the game, the value of each cell will change depending on the other cells around it. This might sound confusing at first, but looks easier when you break it down a bit.
# A cell's "neighbours" are the 8 cells around it.
# If a cell is 'off' but exactly 3 of its neighbours are on, that cell will also turn on - like reproduction.
# If a cell is 'on' but less than two of its neighbours are on, it will die out - like underpopulation.
# If a cell is 'on' but more than three of its neighbours are on, it will die out - like overcrowding.
# Fairly simple, right? This might sound boring, but it can generate fairly complex patterns - this one, for example, is called the Gosper Glider Gun and is designed in such a way that it generates little patterns that fly away from it. There are other examples of such patterns, like ones which grow indefinitely.
# Your challenge is, given an initial 'state' of 'on' and 'off' cells, and a number, simulate that many steps of the Game of Life.
# Formal Inputs and Outputs
# Input Description
# You will be given a number N, and then two more numbers X and Y. After that you will be given a textual ASCII grid of 'on' and 'off' states that is X cells wide and Y cells tall. On the grid, a period or full-stop . will represent 'off', and a hash sign # will represent 'on'.
# The grid that you are using must 'wrap around'. That means, if something goes off the bottom of the playing field, then it will wrap around to the top, like this: http://upload.wikimedia.org/wikipedia/en/d/d1/Long_gun.gif See how those cells act like the top and bottom, and the left and right of the field are joined up? In other words, the neighbours of a cell can look like this - where the lines coming out are the neighbours:
# #-...-  ......  ../|\.
# |\.../  ......  ......
# ......  |/...\  ......
# ......  #-...-  ......
# ......  |\.../  ..\|/.
# |/...\  ......  ..-#-.
# Output Description
# Using that starting state, simulate N iterations of Conway's Game of Life. Print the final state in the same format as above - . is off and # is on.


grid = []
with open("GameOfLife.txt", "r") as f:
    [N, X, Y] = [int(k) for k in f.readline().split()]
    grid = f.read().split()


# Simulate N iterations of Conway's Game of Life.
for n in range(N):
    newGrid = ""
    for x in range(X):
        for y in range(Y):
            # Compute the number of on neighbours.
            onCount = 0
            for i in [(x-1) % X, x, (x+1) % X]:
                for j in [(y-1) % Y, y, (y+1) % Y]:
                    if (i,j) != (x,y) and grid[i][j] == '#':
                        onCount += 1
            # Determine what the new cell should be.
            if grid[x][y] == '.' and onCount == 3:
                newGrid += "#"
            elif grid[x][y] == '#' and onCount not in [2, 3]:
                newGrid += '.'
            else:
                newGrid += grid[x][y]
        newGrid += "\n"
    grid = newGrid.split() # Update the grid.

# Print the result.
print("\n".join(grid))