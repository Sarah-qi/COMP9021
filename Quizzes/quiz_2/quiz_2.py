
# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
from time import sleep

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

sleep(0.001)

nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE

#Reversed this given code, so we can judge its moving direction from left to right
given_code = '0' * nb_of_leading_zeroes + f'{int(code):o}'
reversed_code = reversed(given_code)

#Coordinate its direction of movement and save in a dictionary
move_direction = {'0': (0,1), '1': (1,1), '2': (1,0), '3': (1,-1),\
        '4': (0,-1), '5': (-1,-1), '6': (-1,0), '7': (-1,1)}

#Find the position of this point traveled according to this given rule
#Let initial position be (0,0)
position_x = position_y = 0
list_of_position = [(0,0)]
for i in reversed_code:
    (x,y) = move_direction[i]
    position_x += x
    position_y += y
    if (position_x, position_y) not in list_of_position:
        list_of_position.append((position_x,position_y))
    else:
        list_of_position.remove((position_x,position_y))

#Calculate the smallest and biggest coordinates of x and y respectively
left_x = down_y = 0
right_x = up_y = -1
xx = []
yy = []
for item in list_of_position:
    item_x,item_y = item
    xx.append(item_x)
    yy.append(item_y)

if xx != [] and yy != []:
    left_x = min(xx)
    right_x = max(xx)
    down_y = min(yy)
    up_y = max(yy)

#Print on and off according to its position
for y in range(up_y, down_y - 1, -1):
    for x in range(left_x, right_x + 1, 1):
        if (x,y) in list_of_position:
            print(on, end="")
        else:
            print(off, end='')
    if down_y != y:
        print()

if xx != [] and yy != []:
    print()
