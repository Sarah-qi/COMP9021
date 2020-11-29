# Sample Exam 2


def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)
    if word:
        if len(word) == 1:
            print("'"+word+"'")
        else:
            new_str = word[0]
            print("'",end='')
            for i in range(len(word)-1):
                if word[i] != word[i+1]:
                    new_str += word[i+1]
            print(new_str,end='')
            print("'",end='')
    else:
        print("''")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
