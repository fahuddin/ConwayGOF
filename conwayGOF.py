#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random

def count_neighbors(cellr,cellc,grid):
    count = 0 
    if grid[cellr][cellc] == 1:
        count -= 1
    for b in (range(cellr-1,cellr+2)):
        for i in (range(cellc-1,cellc+2)):
            if grid[b][i] == 1:
                count += 1 
    return count 

def next_gen(grid):
    new_grid = copy(grid)
    for r in range(len(grid)-1):
        for c in range(len(grid[0])-1):
            if grid[r][c] == 1  and count_neighbors(r,c,grid) < 2:
                new_grid[r][c] = 0 
            elif  grid[r][c] == 1 and count_neighbors(r,c,grid) > 3:
                new_grid[r][c] = 0 
            elif grid[r][c] == 0 and count_neighbors(r,c,grid) == 3:
                new_grid[r][c] = 1
    return new_grid 
        

grid1 = [[0,0,0,0,0],
         [0,0,1,0,0],
         [0,0,1,0,0],
         [0,0,1,0,0],
         [0,0,0,0,0]]

grid2 = next_gen(grid1)


                
    
    
    

    