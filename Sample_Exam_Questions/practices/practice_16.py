import sys
from math import sqrt


def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.

    Won't be tested for b greater than 10_000_000

    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''

    prime_list = find_prime_list(a, b)
    first = prime_list[0]
    length = []
    for second in prime_list:
        if second - first - 1 == -1:
            length.append(0)
        else:
            length.append(second - first - 1)
            first = second
    result = max(length)

    print(f'The maximum gap between successive prime numbers in that interval is {result}')

def find_prime_list(m, n):
    l = []
    for i in range(m, n+1):
        if prime_num(i):
            l.append(i)
    return l

def prime_num(e):
    for i in range(2,e):
        if e % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
