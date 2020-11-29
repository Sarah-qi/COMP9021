# Quiz 1 *** Due Friday Week 3 @ 10.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
#Cycles
#delete the numbers, values, which cannot be found through keys
copy_mapping = mapping.copy()
for k in keys:
    if copy_mapping[k] not in keys:
        del copy_mapping[k]
keys = sorted(copy_mapping.keys())
#find the cycles
for k in keys:
    L = []
    while True:
        if copy_mapping[k] == k:
            cycles.append([k])
            break
        if copy_mapping[k] in keys:
            L.append(k)
            k = copy_mapping[k]
            if copy_mapping[k] == k:
                break
            elif copy_mapping[k] == L[0]:
                L.append(k)
                cycles.append(L)
                keys.remove(k)
                break
            elif copy_mapping[k] in L:
                break
        else:
            break

#Reversed dictionary
#only reverse the dictionary
first_reversed_dictionary = {}
keys = sorted(mapping.keys())
values = sorted(mapping.values())
for i in range(len(values)):
    stored_keys = []
    for j in range(len(keys)):
        if values[i] == mapping[keys[j]]:
            stored_keys.append(keys[j])
    first_reversed_dictionary[values[i]] = stored_keys
    
#calculate the length of values in first-reversed_dictionary
length_values = []
for v in first_reversed_dictionary.values():
    length = len(v)
    if length not in length_values:
        length_values.append(length)
        
#reversed_dict_per_length
reversed_dict_per_length = {}
for i in length_values:
    new_dict = {}
    for k in first_reversed_dictionary.keys():
        if len(first_reversed_dictionary[k]) == i:
            new_dict[k] = first_reversed_dictionary[k]
    reversed_dict_per_length[i] = new_dict

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
