
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.


    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''

    sum_list = []
    sum_rows = []
    sum_columns = []
    #每行之和
    for m in square:
        sum_rows.append(sum(i for i in m))
    sum_list.extend(sum_rows)

    #每列之和
    for i in range(len(square)):
        temp = 0
        for j in range(len(square)):
            temp += square[j][i]
        sum_columns.append(temp)
    sum_list.extend(sum_columns)

    #对角线之和
    a = sum(square[i][i] for i in range(len(square)))
    b = sum(square[i][len(square)-1-i] for i in range(len(square)))

    sum_list.append(a)
    sum_list.append(b)

    set_sum = set(sum_list)

    if len(sum_list) == len(set_sum):
        return True
    else:
        return False

    # print(sum_list)
    # print(set_sum)

#求square每行之和
# def sum_rows(square,m):
#     rows = []
#     for m in square:
#         rows.append(sum(i for i in m))
#
#     return rows

if __name__ == '__main__':
    import doctest
    doctest.testmod()

