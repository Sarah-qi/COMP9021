# Quiz 6 *** Due Friday Week 9 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).
# Neighbours are only considered vertically or horizontally (not diagonally).


from random import seed, randrange
import sys
from collections import defaultdict

dim = 10

direction = [(-1,0),(1,0),(0,-1),(0,1)]
nb_of_shapes = defaultdict(list)
colour = 2

def display_grid():
    for row in grid:
        print('   ', *row) 

# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes(i,j,colour):
    #循环开始的条件
    if 0 <= i < 10 and 0 <= j < 10:
        if grid[i][j]==1:
            grid[i][j] = colour
            for two_tuple in direction:
                colour_shapes(i+two_tuple[0],j+two_tuple[1],colour)
    # Replace pass above with your code

def max_number_of_spikes(nb_of_shapes):
    for i in range(10):
        for j in range(10):
            if grid[i][j] > 0:
                nb_of_shapes[grid[i][j]].append((i,j))
    #print(nb_of_shapes)
    max_spikes_num = 0
    #有多少个spikers
    for i in nb_of_shapes:
        spikes = 0
        if len(nb_of_shapes[i]) < 2:
            strike = 0
            continue
        for j in nb_of_shapes[i]:
            m,n = j
            count = 0
            for tup in direction:
                new_i = m + tup[0]
                new_j = n + tup[1]
                if 0 <= new_i < 10 and 0 <= new_j < 10:
                    if grid[new_i][new_j] == grid[m][n]:
                        count = count + 1
            if count == 1:
                spikes = spikes + 1
            max_spikes_num = max(max_spikes_num,spikes)
    return max_spikes_num
    # Replace pass above with your code
# Possibly define other functions here

try:
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]

#给不同shape colour赋予不同的值
for i in range(10):
    for j in range(10):
        if grid[i][j]:
            colour_shapes(i,j,colour)
            colour = colour + 1

print('Here is the grid that has been generated:')
display_grid()
# nb_of_shapes
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
