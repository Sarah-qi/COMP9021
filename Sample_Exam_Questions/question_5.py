# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    file = []
    with open('cpiai.csv') as f:
        for i in f.readlines():
            file.append(i.strip())
        file = file[1:]

    inflation = []
    num_months_list = []
    num_months = []

    for i in file:
        i = i.split(',')
        if i[0][:4] == str(year):
            inflation.append(i[2])
            num_months_list.append(i)

    max_inflation = max(inflation)
    for i in num_months_list:
        if max_inflation == i[2]:
            num_months.append(i[0][5:7])

    alpha_months = ''
    for i in num_months:
        if i == num_months[-1]:
            alpha_months += months[int(i)-1]
        else:
            alpha_months += months[int(i)-1]
            alpha_months += ', '

    print(f'In {year}, maximum inflation was: {max_inflation}')
    print(f'It was achieved in the following months: {alpha_months}')
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
