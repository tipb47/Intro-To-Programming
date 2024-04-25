"""
One of the code implementations for the problems in Lab3.py

I may add some more interesting functions such as append_prime_number
"""

# List Operations

from math import factorial
from modulefinder import packagePathMap
from re import L


def manual_append(list_one, element):
    list_one = list_one + [element]
    return list_one
    '''
    given a list and an element append the element to the list 
    note to do this operation you can't use the .append method for lists

    inputs:
    list_one - a list of values can be any type
    element - a value of any type

    output:
    one coherent list of all elements combined

    '''
    pass

def manual_remove(list_one, val):
    output = []
    for i in range(len(list_one)):
        if list_one[i] != val:
            output = manual_append(output, list_one[i])

    return output

    '''
    given a list and a specific value remove the item and report wether you were successful 
    by using a for loop to iterate over the list

    inputs:
    list_one - list of specific type(int or str) 
    val - the value that you want removed

    output:
    list - the list with the element removed if the element is not found return the list
    '''
    pass

# Doing things with list data structures

def compare_lists(list_one, list_two):
    output = []
    for index in range(len(list_one)):
        if list_one[index] != list_two[index]:
            output = manual_append(output, index)

    return output

    '''
    given 2 lists compare and report which indexes are different in an output list

    your output should look something like this: [1, 3, 5]
    
    which means that index 1, 3, and 5 are different values these lists can compare any data type

    inputs:
    list_one - list of a specific type (int or str) of length n
    list_two - list of a specific type (int or str) of length n

    outputs:
    list of ints which correlate to indexes that are different in a list
    '''
    

def factorial_for(n):

    output = 1

    for i in range(1, n+1):
        output *= i

    return output


    '''
    given a number calculate the factorial value using a for loop

    input:
    n - integer value that will be factorial you want to calculate 

    output:
    the calculated factorial of the input value 
    '''
    pass


if __name__ == '__main__':
    
    print(manual_append([1, 2, 3, 4], 100))
    print(manual_remove([1, 2, 3, 4], 3))
    print(compare_lists([1,2,3,4], [1,9,3,10]))
    print(factorial_for(5))
    
    # TODO:
    # implement testing
    pass
    
    
