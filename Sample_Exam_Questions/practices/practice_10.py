
def number_of_words_in_dictionary(word_1, word_2):
    '''
    "dictionary.txt" is stored in the working directory.
    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''
    
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    with open('dictionary.txt') as filename:
        dict_list = []
        for line in filename.readlines():
            line = line.strip()
            dict_list.append(line)
        if word_1 == word_2:
            if word_1 not in dict_list:
                print(f'Could not find {word_1} in dictionary.')
            else:
                print(f'{word_1} is in dictionary.')
        elif word_1 not in dict_list or word_2 not in dict_list:
            print(f'Could not find at least one of {word_1} and {word_2} in dictionary.')
        else:
            if dict_list.index(word_1) <= dict_list.index(word_2):
                n1 = dict_list.index(word_1)
                n2 = dict_list.index(word_2)
                new_list = dict_list[n1:n2+1]
                print(f'Found {len(new_list)} words between {word_1} and {word_2} in dictionary.')
            else:
                n1 = dict_list.index(word_2)
                n2 = dict_list.index(word_1)
                new_list = dict_list[n1:n2+1]
                print(f'Found {len(new_list)} words between {word_1} and {word_2} in dictionary.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
