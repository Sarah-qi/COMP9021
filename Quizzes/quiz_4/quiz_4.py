
# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a strictly positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys
from time import sleep

def encode(list_of_integers):
    # REPLACE pass ABOVE WITH YOUR CODE
    first_binary = []
    for i in list_of_integers:
        first_binary.append(bin(i)[2: ])
    next_binary = str(first_binary).replace('1','11')
    next_binary = (str(next_binary).replace('0','00')).replace(',','0')
    real_binary = ''.join([i for i in next_binary if i.isdigit()])
    decimal_number = int(real_binary, 2)
    return decimal_number

def decode(integer):
    # REPLACE pass ABOVE WITH YOUR CODE
    first_binary = bin(integer)[2: ]
    num_index = 0
    separate_binary = ''
    while num_index < len(first_binary):
        try:
            if first_binary[num_index] == first_binary[num_index+1]:
                separate_binary += first_binary[num_index]
                num_index += 2
            elif first_binary[num_index] == '1' and first_binary[num_index+1] == '0':
                return None
                break
            elif first_binary[num_index] == '0' and first_binary[num_index+1] == '1':
                separate_binary += ','
                num_index += 1
        except:
            return None
    final_decimal = []
    while ',' in separate_binary:
        _index_ = separate_binary.find(',')
        final_decimal.append(int((separate_binary[:_index_]),2))
        separate_binary = separate_binary[_index_+1:]
    final_decimal.append(int(separate_binary,2))
    return final_decimal

# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
sleep(0.001)

if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
