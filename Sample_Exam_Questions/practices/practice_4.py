# Sample Exam 2


'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''

import numpy as np

def find_word(filename, word):
    '''
    >>> find_word('word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    with open(filename) as file:
        grid = []
        for i in file:
            grid.append(i.rstrip())

        if len(grid) > 14:
            new_grid = []
            for i in grid:
                for j in i:
                    if j != " ":
                        new_grid.append(j)
            new_grid = np.array(new_grid)
            new_grid = new_grid.reshape((14,14))

            n_grid = []
            for i in new_grid:
                temp = ''
                for j in i:
                    temp += j
                n_grid.append(temp)
            grid = n_grid

        # Insert your code here
        # A one liner that sets grid to the appropriate value is enough.
        location = find_word_horizontally(grid, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(grid, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(grid, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')


def find_word_horizontally(grid, word):
    for i in range(len(grid)):
        if word in grid[i]:
            y = grid[i].index(word) + 1
            x = i + 1
            return (x,y)
    # Replace pass above with your code


def find_word_vertically(grid, word):
    T_grid = []
    for i in range(len(grid[0])):
        temp = []
        for j in range(len(grid)):
            temp.append(grid[j][i])
        temp = ''.join(temp)
        T_grid.append(temp)
    #T_grid = np.array(T_grid)
    #print(T_grid)
    for i in range(len(T_grid)):
        if word in T_grid[i]:
            x = T_grid[i].index(word) + 1
            y = i + 1
            return (x,y)
    # Replace pass above with your code


def find_word_diagonally(grid, word):
    for x_index in range(len(grid)-len(word)+1):
        new_x = x_index
        for y_index in range(len(grid)-len(word)+1):
            new_y = y_index
            find_word = ''
            count = 0
            while count < len(word):
                find_word += grid[new_x][new_y]
                count += 1
                new_x += 1
                new_y += 1
            new_x = x_index
            if find_word == word:
                x = x_index + 1
                y = new_y - len(word) + 1
                return (x,y)
    # Replace pass above with your code


if __name__ == '__main__':
    import doctest
    doctest.testmod()
