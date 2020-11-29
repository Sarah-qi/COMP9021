# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.

    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''


    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    new_list = []
    alpha = 'a'
    for i in range(height):
        temp = ''
        for j in range(width):
            temp += alpha
            if alpha == 'z':
                alpha = 'a'
            else:
                alpha = chr(ord(alpha)+1)
        new_list.append(temp)

    for i in range(height):
        if i % 2 != 0:
            new_list[i] = new_list[i][::-1]

    for i in new_list:
        print(i)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
