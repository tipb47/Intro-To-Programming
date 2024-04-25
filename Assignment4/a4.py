
import math

#Problem 1  DONE
#INPUT list of 0 and 1
#RETURN the COUNT of the longest sequence of concecutive 1s is returned
def ls(x):
    count = 0
    longest = 0
    for i in x:
        if i == 1:
            count += 1
            if count > longest:
                longest = count
        if i == 0:
            count = 0

    return longest



###########################################################################
# Problem 2  DONE
###########################################################################

#INPUT two lists of 0s and 1s. Think of each list as representing a person
# as explained in the HW PDF.
#RETURN inner product.
def inner_prod(v0, v1):
    sum = 0
    for i in range(len(v1)):
        sum += (v0[i]*v1[i])
    return sum


#INPUT a list of 0s, 1s
#RETURN square root of inner product
def mag(v):
    return math.sqrt(inner_prod(v,v))

#INPUT two lists of 0s, 1s 
#RETURN angle in degrees
def angle(v0, v1):
    num = inner_prod(v0,v1)
    denom = mag(v0)*mag(v1)
    return round(((180/math.pi)*(math.acos(num/denom))), 2)

#INPUT list of people
#RETURN unique pairs with angle
def match(people):
    list = []
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            list += [[people[i], people[j], angle(people[i],people[j])]]
    return list

#INPUT list of pairs with angle
#RETURN best pair (smallest angle)
def best_match(scores):
    smallest = scores[0][2]
    for i in scores:
        if smallest == None:
            smallest = i[2]
            continue
        if i[2] <= smallest:
            smallest = i[2]
            bestpair = i
    return bestpair

            




###########################################################################
# Problem 3  DONE
###########################################################################
#INPUT two lists like [m ,b]. Each list represents a line in slop, intercept form.
#RETURN 2D point of intersection in the format [x-coordinate, y-coordinate].
def intersect(d0, d1):
    xcoord = (d0[1] - d1[1])/(d1[0] - d0[0])
    ycoord = (d0[0] * xcoord) + d0[1]
    return [round(xcoord,2),round(ycoord,2)]

###########################################################################
# Problem 4  DONE
###########################################################################
#INPUT list of numbers
#RETURN dictionary of relative frequency of members in the list
def make_prob(xlst):
    dict = {}
    for i in xlst:
        freq = round(xlst.count(i)/len(xlst),2)
        dict[i] = freq
    return dict

###########################################################################
# Problem 5  DONE
###########################################################################
#INPUT list of numbers
#RETURN entropy of probability function
def entropy(lst):
    pmf = make_prob(lst)
    sum = 0
    for i in pmf:
        pi = pmf[i]
        sum += -(pi * math.log(pi, 2))
    return round(sum,2)


###########################################################################
# Problem 6  DONE
###########################################################################
#INPUT List of numbers
#RETURN mean
def mean(lst):
    total = 0
    for i in lst:
        total += i
    return round(total/len(lst),2)

#INPUT list of numbers
#RETURN variance
def variance(lst):
    m = mean(lst)
    total = 0
    for i in lst:
        total += (i - m)**2

    return round((1/len(lst))*total,2)


#INPUT list of numbers
#RETURN standard deviation (sqrt of variance)
def std(lst):
    return round(math.sqrt(variance(lst)),2)


#INPUT list of numbers
#RETURN list of mean centered numbers 
def mean_centered(lst):
    newlst = []
    m = mean(lst)
    for i in lst:
        newlst = newlst + [i-m]
    return newlst



###########################################################################
# Problem 7  DONE
###########################################################################
#INPUT list of numbers and option 0, 1
#RETURN absolutest greatest difference if option = 1, and smallest if option = 0
def blist(lst):

    lst[0].sort()
    lastNum = len(lst[0])-1

    if lst[1] == 1: #largest abs distance
        return lst[0][lastNum] - lst[0][0]

    if lst[1] == 0: #smallest abs distance
        for i in lst[0]:
            if i < 0:
                lst[0].pop(i)
        return lst[0][1] - lst[0][0]


###########################################################################
# Problem 8  DONE
###########################################################################
#INPUT lists of data logs [name,[s1,t1],[s2,t2],...]
#RETURN the name and most mileage
def f_(xlst):
    most = 0
    mostName = 'placeholder'
    for i in xlst:

        name = i[0]
        total = 0

        for j in i[1:]:
            
            if len(j[1]) == 1:
                total += j[0] * j[1][0]

            if len(j[1]) == 2:
                hrs = j[1][0]
                mins = j[1][1]
                dist = hrs + (mins/60)
                total += j[0] * dist
                if total > most:
                    most = total
                    mostName = name

    return [mostName, most]

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    If you uncomment the following print statements for testing
    then please comment them back before submitting your final version.

    You are encouraged to do some of your own testing by
    trying different values as function parameters in the print 
    statements.
    """

    # #problem 1
    # p1 = [[0,1,1,0,0,0,1,1,1,1],[0,0],[1,1,0,1],[1,1,0,1,1,1,1],
        #   [1,1,1,1,1,1,1,1,1,1,1], [0,0,1,1,1,1,0,0]]
    # for x in p1:
        # print(f"{x}  {ls(x)}")

    #problem 2
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
            #    [1,1,0,1,1,1,0],
            #    [1,0,1,1,0,1,1],
            #    [1,0,0,1,1,0,0],
            #    [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    
    # v0,v1 = (2,3,-1),(1,-3,5)
    # print(f"122 deg = {angle(v0,v1)}") #122

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(f"85.41 deg = {angle(v0,v1)}") #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(f"70.53 deg = {angle(v0,v1)}") #70.53

# 
    # #problem 3
    # l0 = (2,3)
    # l1 = (-1/2,2)
    # print(intersect(l0,l1)) #-2/5,11/5
    # print(intersect((1,4),(-1/2,1/2)))
 
    #problem 4
    # p4 = [[1,1,0,0],[1,2,3,1,1,2,1],['a','a','b']]

    # for d in p4:
        # print(f"{d} {make_prob(d)}")
    
    # #problem 5
    # p5 = [[1,1,0,0],[1,2,3,1,1,2,1],['a','a','b']]
    # for d in p5:
        # print(f"{entropy(d)}")

    # #problem 6
    # p6 = [1,3,3,2,9,10]
    # print(f"mean {mean(p6)}")
    # print(f"variance {variance(p6)}")
    # print(f"std {std(p6)}")
    # print(f"mean centered {mean(mean_centered(p6))}")

    # # problem 7
    # p7 = [[[6,2,1,100],1],[[6,2,1,100],0],[[0,0,10,10],1],
    #    [[1,2,1,-4],0],[[1,2,1,-4],1],[[0,0,10,10],0]]
    # for d in p7:
        # print(f"{d} {blist(d)}")

    # #problem 8
    # truck_d = [['X', [ 55,[0,60]],[15,[2.5]],[75,[.2,48]]],
        #    ['Y', [55,[0,60]]],
        #    ['Z', [10,[1]],[10,[1]]],
        #    ['A', [30,[2]]]]
    # print(f"{f_(truck_d)}")