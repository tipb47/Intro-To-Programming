import math
from re import A

#problem 1
#input real
#return real
def g(x):
    if x != 0:
        return x + 2
    else:
        return 1


#problem 2
#input year 1977-1997
# return percent income or "error: year" if year 
# is outside range
def f(t):
    if t >= 1977 and t <= 1984:
        return 2/7*(t - 1977) + 12
    elif t > 1984 and t <= 1987:
        return (t - 1977) + 7
    elif t > 1987 and t <= 1997:
        return 3/5*(t - 1977) + 11
    else:
        return "error: year"


#problem 3
#input t years = 0
#output dollars
def h_0(t):
    return 110/((1/2)*t + 1)

def h_1(t):
    return 26*((1/4)*t**2 - 1)**2 + 52
def h(t):
    return h_0(t) - h_1(t)


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    x_1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    x_2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
    tuple = (x_1, x_2)
    return tuple

#problem 5
#input [arg1,op,arg2,ans]
#output boolean True or False
def eq(lst):
    arg1 = lst[0]
    op = lst[1]
    arg2 = lst[2]
    ans = lst[3]

    if op == "*":
        equation = arg1*arg2
    elif op == "+":
        equation = arg1+arg2
    elif op == "-":
        equation = arg1-arg2
    elif op == "/":
        equation = arg1/arg2

    if equation == ans:
        return True
    else:
        return False

#problem 6
#input list of swithes
#output True if path from start to end
def path(lst):
    switch0 = lst[0]
    switch1 = lst[1]
    switch2 = lst[2]
    switch3 = lst[3]
    switch4 = lst[4]
    if switch0 == True:
        if switch2 == True:
            return True
        if switch1 == True:
            if switch3 == True or switch4 == True:
                return True
    else:
        return False

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x, y):
    if x > y:
        return x
    else:
        return y

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x, y, z):
    return max2d(x,max2d(y,z))

#PROBLEM 8
#INPUT dimension x and area A
#OUTPUT length of fence
def f_(x, A):
    y = (A/x)
    print(y)
    return (2*y) + (2*x)

#INPUT x dimension and length of fence
#OUTPUT y dimension
def g_(x, length_of_fence):
    y = (length_of_fence-(2*x))/2
    return y

#PROBLEM 9
#INPUT x dimension of box with 20 ft**3 volume
#OUTPUT cost in dollars
def box_cost(x):
    y = 20/(2*x)

    base = (2*x) * .30
    top = (2*x) * .20
    sides = ((x*y) * .10) * 4

    cost = base + top + sides
    return cost

#PROBLEM 10
#INPUT month = 0,1,..., 11
#OUPUT occupancy rate 0..100
def r(month):
    return round((10/81)*month**3 - (10/3)*month**2 + (200/9)*month + 55, 2)

#INPUT occupancy rate 0..100
#OUPUT Revenue generated
def R(r):
    return (((-3/5000)*r**3 + (9/50)*r**2))*1000




if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing. Feel free to add print statements. 
    You should uncomment the print statements *after* you're done testing here.
    """
    #problem 1 
    # print(f"g(0) = {g(0)}")
    # print(f"g(1) = {g(1)}")
    # print(f"g(1.01) = {g(1.01)}")

    #problem 2
    # print(f"f(1976) = {f(1976)}")
    # print(f"f(1977) = {f(1977)}")
    # print(f"f(1985) = {f(1985)}")
    # print(f"f(1988) = {f(1988)}")
    # print(f"f(2000) = {f(2000)}")

    #problem 3
    # print(f"h(0) = {h(0)}")
    # print(f"h(1) = {h(1)}")
    # print(f"h(2) = {h(2)}")

    #problem 4
    # print(f"q((1,0,-1)) = {q((1,0,-1))}")
    # print(f"q((6,-1,-35)) = {q((6,-1,-35))}")
    # print(f"q((1,-7,-7)) = {q((1,-7,-7))}")

    #problem 5
    # print(eq([14, "/",2, 7]))
    # print(eq([20, "*",19, 381]))
    # print(eq([20, "*",19, 380]))

    #problem 6
    # print(f"path([1,0,1,0,0]) = {path([1,0,1,0,0])}")
    # print(f"path([1,1,1,0,0]) = {path([1,1,1,0,0])}")
    # print(f"path([1,0,0,1,0]) = {path([1,0,0,1,0])}")

    #problem 7
    # print(max3d(1,2,3))
    # print(max3d(1,3,2))
    # print(max3d(3,2,1))

    # problem 8
    # A = 250  
    # x0,x1 = 10,20

    # length_of_fence = f_(x0,A)
    # y = g_(x0,length_of_fence)

    # print(f"{x0} x {y} ft^2 with {length_of_fence} ft of fence")

    # length_of_fence = f_(x1,A)
    # y = g_(x1,length_of_fence)
    # print(f"{x1} x {y} ft^2 with {length_of_fence} ft of fence")

    #problem 9
    # x = 2
    # print(f"cost for x = {x}ft is ${box_cost(2)}")

    # problem 10
    # january,june = 0,5
    # print(f"Jan occupancy is {r(january)}%")
    # print(f"Jan revenue: ${R(r(january))}")

    # print(f"Jun occupancy is {r(june)}%")
    # print(f"Jun revenue: ${R(r(june))}")