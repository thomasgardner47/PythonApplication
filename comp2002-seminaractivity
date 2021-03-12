import numpy as np 
import matplotlib.pyplot as plt

def gameofLife(grid, niter):
    grids = [grid] # Python list containing the first list.
    N = grid.shape[0] # Number of rows 

    #iterate
    for itr in range(niter-1):
        nextGrid = np.seros((N,N))

        for i in range(N):
            for j in range(N):
                I = [i-1, i, (i+1)%N] * 2 + [i-1, (i+1)%N]
                J = [j-1] * 3 + [(j+1)%N]*3  [j,j]
                neighbours = grid[I,J]

                #Transition rules.
                if grid[i,j] == 1 and sum(neighbours) < 2:
                    nextGrid[i,j] = 0
                if grid [i,j] == 1 and sum(neighbours) in [2,3]:
                    nextGrid[i,j] = 1
                if grid[i,j] == 1 and sum(neighbours) > 3:
                    nextGrid[i,j] = 0
                if grid[i,j] == 0 and sum(neighbours) == 3:
                    nextgrid[i,j] = 1

            # Append the grid to the List, and update the nextGrid
            # to be 