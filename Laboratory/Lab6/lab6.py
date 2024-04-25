###########################################################
# factorial
###########################################################

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    

def tail_factorial(n, a=1):
    if n == 0:
        return a
    else:
        return tail_factorial(n-1, a=a*n)

    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    

d = {}
def memo_factorial(n):
    if n not in d.keys():
        if n == 1:
            d[n] = 1
        else:
            d[n] = n * memo_factorial(n-1)
    return d[n]
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    

###########################################################
# only_ints
###########################################################

def only_ints(xlist):
    if xlist == []:
        return []
    if type(xlist[0]) != int:
        return [] + only_ints(xlist[1:])
    else:
        return [xlist[0]] + only_ints(xlist[1:])

    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    

def tail_only_ints(xlist, a=[]):
    if xlist == []:
        return a
    if type(xlist[0]) != int:
        return a + only_ints(xlist[1:])
    else:
        return [xlist[0]] + only_ints(xlist[1:])

    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """

d = {}
def memo_only_ints(xlist):
    if "dlist" not in d.keys():
        if xlist == []:
            d["dlist"] = []
        if type(xlist[0]) != int:
            d["dlist"] = [] + only_ints(xlist[1:])
        else:
            d["dlist"] = [xlist[0]] + only_ints(xlist[1:])
    return d["dlist"]
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    

if __name__ == "__main__":
    # Write your own print statements here
    print(factorial(5))
    print(tail_factorial(5))
    print(memo_factorial(5))

    print("---------------------------------------------------")

    print(only_ints([1,2,"moo",4,"hello",6,"dog","cat",2]))
    print(tail_only_ints([1,2,"moo",4,"hello",6,"dog","cat",2]))
    print(memo_only_ints([1,2,"moo",4,"hello",6,"dog","cat",2]))
    # to briefly test your code
    