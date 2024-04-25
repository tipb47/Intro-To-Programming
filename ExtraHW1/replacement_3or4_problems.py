import math

# leave unchanged if working individually
# My Partner is ________________________


# problem 1  DONE
# input 0,1,2,...
# return factorial
def factorial(n):
    sum = 1
    if n >= 0:
        for i in range(2, n+1):
            sum *= i
        return sum
    if n < 0:
        for i in range(2, abs(n)+1):
            sum *= -i
        return sum

# problem 2  DONE
# input two lists (containing numbers) of same length
# return a list of the greater number at each position of the input lists 
def gl(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        if lst1[i] >= lst2[i]:
            result += [lst1[i]]
        else:
            result += [lst2[i]]
    return result




#problem 3  DONE
#INPUT argument n and number of terms
#RETURN approximation of e(n) for num_terms.
def my_e(n,num_terms):
    sum = 0
    for i in range(num_terms+1):
        sum += (n**i)/factorial(i)
    return sum

# problem 4
#INPUT a string
#RETURN a dictionary of all the proper substrings with counts of occurences
def ss(x):
    pass

# problem 5  DONE
#INPUT old, new, list of lists
#RETURN for each list in list, replace old with new
def lst_replace(old,new,lst):
    replacedLst = []
    for i in lst:
        lstinlst = []
        for j in i:
            if j == old:
                j = new
            lstinlst.append(j)
        replacedLst += [lstinlst]
    return replacedLst


# problem 6
#INPUT list 
#INPUT remove any list brackets objects are in the same order
def foo(lst):
    pass


if __name__ == "__main__":

    """uncomment if you'd like"""

    # #problem 1
    # for i in range(6):
        # print(f"{i}! = {factorial(i)}")

    # #problem 2
    # p2 = [[[1,0,0,1],[0,1,1,0]],[[],[]],[[1,2,3,4],[5,4,3,2]]]

    # for x,y in p2:
        # print(f"{x,y} {gl(x,y)}")

    # #problem 3
    # print(math.exp(5))
    # print(my_e(5,16))

    # #problem 4
    # p4 = ["s","abc","abcabc","aa"]
    # for d in p4:
    #     print(d)
    #     print(ss(d))

    # #problem 5
    # lst = [[1,2],[2,[2],1],[],[1,1,]]
    # print(lst_replace(1,"dog", [[1,2],[2,[2],1],[],[1,1,]]))
    # print(lst_replace(2,"dog", [[1,2],[2,[2],1],[],[1,1,]]))
    # print(lst_replace([2],"dog", [[1,2],[2,[2],1],[],[1,1,]]))
    # print(lst_replace(1,"dog", []))

    # #problem 6
    # p6 = [[[1],2,[[3]]], [[1,[2,[3]],4,[[5]],6,[7,8]]],
        # [1,2,3,[[[4]]]],[],[1,2,3]]

    # for d in p6:
        # print(f"{d} \n {foo(d)}")
