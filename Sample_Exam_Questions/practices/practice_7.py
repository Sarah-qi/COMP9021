# Sample Exam Question 4
 

'''
Will be tested with a at least equal to 2 and b at most equal to 10_000_000.
'''
    

import sys
from math import sqrt

#判断x是否是质数
def is_prime(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).
    You can assume that "number" is an integer at least equal to 2.
    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''

    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    factors = {}
    # Insert your code here

    #求一个数的质数分解
    n = number
    result = 1
    for i in range(2,number+1):
        v = 0
        while n % i == 0:
            v += 1
            n //= i
            factors[i] = v
            
        if n == 1:
            break

    for k in factors.keys():
        result *= k
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

