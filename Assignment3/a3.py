import math
import numbers

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    size = n_0 * math.exp(m*t)
    return size

#INPUT t days
#RETURN number of teeth
def N_t(t):
    numTeeth = 71.8 * math.exp(-8.96 * math.exp(-0.0685 * t))
    return math.ceil(numTeeth)

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    workJoules = 8.314*300 * math.log(P_i/P_f)
    return math.ceil(workJoules)


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    lbs = 0.0033 * V**2 * A * C_l
    return math.ceil(lbs)

###########################################################################
# Function for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN True if discriminant is real, False otherwise
def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    if b**2 - 4*a*c > 0:
        return True
    else:
        return False


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT item and list
#RETURN True if item is in the list
#CONSTRAINT You cannot use 'in' -- must use bounded looping.
def m(x,lst):
    status = False
    for i in lst:
        if i == x:
            status = True
    return status
            
        

def amt(r,no_tax):
    total = 0
    for item,price in r:
        total += price
        if m(item, no_tax) != True:
            total += price*0.07
    return round(total,2)

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN (m, b) for line y = mx + b
def f(p0, p1):
    if p0[0] == p1[0]:
        return ()
    else:
        m = (p1[1] - p0[1])/(p1[0] - p0[0])
        b = (p0[1]) - (m*p0[0])
        return (m, b)


###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

# Use these error messages according to the case that you encounter.
# You can use them err_msg[0] or err_msg[1].
# Make sure that you don't change the error messages. 
# Use them as such without alterations.
err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    count = 0
    if nlst == []:
        return err_msg[0]
    for i in range(len(nlst)):
        count += nlst[i]
    return round(count/len(nlst),2)

def geo_mean(nlst):
    count = 0
    if nlst == []:
        return err_msg[0]
    for i in nlst:
        if i == 0:
            return err_msg[1]
        count += math.log(i,10)
    return round(10**(count/len(nlst)), 2)

def har_mean(nlst):
    count = 0 
    if nlst == []:
        return err_msg[0]
    for i in range(len(nlst)):
        if nlst[i] == 0:
            return err_msg[1]
        count += 1/nlst[i]
    return round((len(nlst)/count),2)
    

def RMS_mean(nlst):
    sum = 0
    if nlst == []:
        return err_msg[0]
    for i in range(len(nlst)):
        sum += nlst[i]**2
    return round(math.sqrt(sum/len(nlst)),2)

###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def F(x):
    return 10000

#INPUT x filters
#RETURN variable cost
def V(x):
    if x >= 0 and x <= 40000:
        return -0.0001*x**2 + 10*x
    else:
        return 0

#INPUT x filters
#RETURN total cost
def C(x):
    return V(x) + F(x)



###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT list [p,i,n] principal, interest rate, number of years
#RETURN monthly payment amount
def Mortgage(house):
    p = house[0]
    i = (house[1] * .01)/12
    n = house[2] * 12
    m = p * ((i*(1 + i)**n)/(((1 + i)**n) - 1))
    return round(m,2)


#INPUT list [p,i,n] principal, interest rate, number of years
#RETURN the difference between total paid and actual value of home
#REQUIRES Use Mortgage function
def total_paid(house):
    return round(((Mortgage(house))*(30)*(12)) - 300000,2)
    


###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT first two members of geometric series and list size
#RETURN returns a list of geometric series of list size
def geo(lst, n):
    for i in range(n-2):
        f = lst(len(lst)- 1)
        num = lst(len(lst)- 1)
        den = lst(len(lst)- 2)
        lst += f * (num/den)
    return lst



###########################################################################
# Functions for Problem 9
###########################################################################
# A
#INPUT first two members of geometric series and list size
#RETURN returns a list of geometric series of list size
def two_min(lst):
    lst.sort()
    return [lst[0], lst[1]]

###########################################################################
# B
#INPUT list of numbers
#RETURN A list of the maximum and number of times it appears or empty list
def mm(lst):
    max = -1111111
    count = 0
    if lst == []:
        return []
    for i in lst:
        if i > max:
            max = i
    for j in lst:
        if j == max:
            count += 1
    return [max, count]


###########################################################################
# C
#INPUT list of numbers
#RETURN true if list is monotonic, false otherwise
def mo(lst):
    nlst = []
    nlst.extend(lst)
    lst.sort()
    if nlst == lst:
        return True
    return False


###########################################################################
# D
#INPUT list of weights and weight
#RETURN the list of weights greater than or equal 
def w(classes, wt):
    result=[]
    for i in classes:
        if type(i) == str:
            result.append(i)
            return result
        if i >= wt:
            result.append(i)

###########################################################################
# F
#INPUT two tuples represeting the points
#RETURN the distance between the points 
def dis(p0, p1):
    count = 0
    total = 0
    while (len(p0)-1) != count:
        total += (p0[count] - p1[count])**2
        count += 1
    return math.sqrt(total)

###########################################################################
# G
#INPUT list of points (point is represented by a tuple)
#RETURN Total distance
def trip(lst):
    count = 0
    distance = 0
    while count < len(lst) - 1:
        count += 1
        distance += dis(lst[count], lst[count+1])
    return distance


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please uncomment the print statements below. You are encouraged to
    write some of your own tests here or in the a3_test.py file.

    Remember to comment the print statements below after you are done 
    testing.
    """
    
    # #problem 1
    # print(N(500,100,4)) 
    # print(N_t(1000))
    # print(W(10,1))
    # print(L(33.8,512,0.515))
# 
    #problem 2
    # print(q((1,4,-21)))
    # print(q((3,6,10)))
    # print(q((1,0,-4)))

    #problem 3
    # receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    # no_tax = [33,5,2]
    # print(amt(receipt,no_tax))

    # #problem 4
    # print(f((2,3),(6,4)))
    # print(f((1,6),(3,2)))
    # print(f((1,3),(1,5)))
 
    #problem 5
    # print(arithmetic_mean([1,2,3]))
    # print(geo_mean([2,4,8]))
    # print(har_mean([1,2,3]))
    # print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # print(C(0))
    # print(C(100))
    # print(C(1000))

    #problem 7
    house = [300000,2.9,30]
    print(Mortgage(house))
    print(total_paid(house))

    # #problem 8
    # data = [[1,-3],[2,6],[10,5],[math.sqrt(2),-math.sqrt(2)]]
    # for d in data:
        # print(geo(d,4))

    # #problem 9

    # A
    # data = [[5,4,3,2,1],[1,2],[1,4,2,0,1,100],[5,0,0,5],[1,2,3,4,5]]
    # for d in data:
        # print(f"{two_min(d)}")
# 
    # B
    # data = [[],[1],[2,1,2,1,2],[0,1,100],[1,2,3,1,2,3,3,5]]
    # for d in data:
        # print(f"{d} {mm(d)}")
# 
    # C 
    # data = [[1],[1,1.1,1.1,1.3,2],[20,21,22,23,22,24],[1,10],[10,1]]
    # for d in data:
        # print(f"{mo(d)}")
# 
    # D
    # classes = [125,133,141,149,157,165,174,184,197,"HW"]
    # wts = [110,163,166,184,197,198]
    # for w_ in wts:
        # print(f"{w(classes,w_)}")

    # E
    # data = [[(1,2,3,1),(4,2,3,2)],[(1,2),(3,1)],[(3,),(2,)]]
    # for p0,p1 in data:
        # print(f"{dis(p0,p1)}") 
# 
    # F
    # data = [[(1,),(3,),(7,)],[(1,1)],[(0,0),(1,0),(1,1),(1,2)],[(0,0,0),(1,1,1)]]
    # for d in data:
        # print(f"{trip(d)}")
