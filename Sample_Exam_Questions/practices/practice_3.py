# Sample Exam 2


'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''

from itertools import combinations,permutations
def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    list = []
    word_list = ['']
    if not word:
        print([word])
    elif len(word) == 1:
        print(['',word])
    else:
        list.append(word[0])
        if word[1:]:
            for i in range(len(word)-1):
                if word[i] != word[i+1]:
                    list.append(word[i+1])
        #print(list)
        set_list = sorted(set(list))
        #print(set_list)
        for length in range(1,len(set_list)+1):
            word_list.extend(justify_sequences(list,length))

        print(sorted(word_list))

# Possibly define another functions
def justify_sequences(l,n):
    temp = []
    for i in list(combinations(l,n)):
        i = ''.join(i)
        j = set(i)
        if i not in temp and len(j) == len(i):
            temp.append(i)
    return temp


if __name__ == '__main__':
    import doctest
    doctest.testmod()

