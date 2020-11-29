# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''

    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    if not word:
        return ''
    elif len(word) == 1:
        return word
    else:
        list = []
        first = word[0]
        temp = first

        for i in word[1:]:
            if ord(i) == ord(temp[-1]) + 1:
                temp += i
            else:
                list.append(temp)
                temp = i
        list.append(temp)

        length = []
        for i in list:
            length.append(len(i))

        max_length = max(length)
        for i in list:
            if len(i) == max_length:
                return i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
