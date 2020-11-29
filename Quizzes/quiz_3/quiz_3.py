# Quiz 3 *** Due Friday Week 5 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends and
#   around parentheses and commas, is a valid word.

import sys
from time import sleep


def is_valid(word, arity):
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    #Identify a valid symbol
    valid_symbol = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
                        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sign = ['_', '(', ')', ',']
    for i in word.strip():
        if (i not in valid_symbol) and (i not in sign) and (i != ' '):
            return False
            
    #If arity == 0, 检查symbol是否合法
    if arity == 0:
        if (not word.strip()) or ' ' in word.strip():
            return False
        for i in word.strip():
            if i not in valid_symbol:
                return False
        return True
        
    #If arity != 0, if there is no '(' or ')', return false
    if arity != 0 and word.strip():
        if (word.strip())[0] not in valid_symbol or (word.strip())[-1] != ')':
            return False
        if ('(' and ')') not in word.strip():
            return False
        elif word.count('(') != word.count(')'):
            return False
            
    #Start to identify whether the symbol inside symbol satisfy the requirements
    while ')' in word.strip():
        right_parenthesis_index = (word.strip()).find(')')
        left_parenthesis_index = (word[:right_parenthesis_index]).rfind('(')
        if left_parenthesis_index > right_parenthesis_index:
            return False
        else:
            part_split = ((word[left_parenthesis_index+1:right_parenthesis_index]).strip()).split(',')
            count_element = 0
            for i in part_split:
                if (not i) or i.isspace() or (' ' in i.strip()):
                    return False
                for j in i.strip():
                    if not j:
                        return False
                    if j not in valid_symbol:
                        return False
                count_element += 1
            if count_element != arity:
                return False
            elif right_parenthesis_index < word.rfind(')'):
                if word[left_parenthesis_index-1].isalpha() and word[right_parenthesis_index+1].isalpha():
                    return False
                elif word[left_parenthesis_index-1].isalpha() and word[right_parenthesis_index+1]=='(':
                    return False
                else:
                    word = word[:left_parenthesis_index]+word[right_parenthesis_index+1:]
            else:
                word = word[:left_parenthesis_index]
    if word.strip():
        if ' ' in word.strip():
            return False
        for i in word.strip():
            if i not in valid_symbol:
                return False
        return True
    else:
        return False

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
sleep(0.001)
