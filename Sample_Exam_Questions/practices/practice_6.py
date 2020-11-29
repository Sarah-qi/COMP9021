from math import log, ceil, sqrt


# Prints out all lines of the form k = b^p such that:
# - m <= k <= n
# - p >= 2
# from smallest k to largest k and for a given k,
# from smallest b to largest b.
#
# No indication on the range of values to be tested,
# just do your best...
#
# You can assume that m and n are positive integers.
def f(m, n):
    '''
    >>> f(10000, 1)
    >>> f(17, 21)
    >>> f(17, 210)
    25 = 5^2
    27 = 3^3
    32 = 2^5
    36 = 6^2
    49 = 7^2
    64 = 2^6
    64 = 4^3
    64 = 8^2
    81 = 3^4
    81 = 9^2
    100 = 10^2
    121 = 11^2
    125 = 5^3
    128 = 2^7
    144 = 12^2
    169 = 13^2
    196 = 14^2
    >>> f(110500, 117700)
    110592 = 48^3
    110889 = 333^2
    111556 = 334^2
    112225 = 335^2
    112896 = 336^2
    113569 = 337^2
    114244 = 338^2
    114921 = 339^2
    115600 = 340^2
    116281 = 341^2
    116964 = 342^2
    117649 = 7^6
    117649 = 49^3
    117649 = 343^2
    >>> f(34359738368, 34359848368)
    34359738368 = 2^35
    34359738368 = 32^7
    34359738368 = 128^5
    34359812496 = 185364^2
    34359822251 = 3251^3
    '''
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    if m > n:
        return

    result = []
    for k in range(m, n+1):
        for b in range(2, n):
            p = 2
            while p < n:
                if k == b ** p:
                    result.append((k, b, p))
                    break
                else:
                    p += 1
    if not result:
        return

    for i in result:
        if i == result[-1]:
            print(f'{i[0]}={i[1]}^{i[2]}',end='')
        else:
            print(f'{i[0]}={i[1]}^{i[2]}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

#f(34359738368, 34359848368)
