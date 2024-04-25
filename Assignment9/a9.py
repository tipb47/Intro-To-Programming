import math 
#PROBLEM 1
#INPUT a function f(x)
#RETURN a function lambda x: (f(x+h) - f(x-h))/(2h)
# where h = .00001
# Note, in this function we are not returning a numeric value, but a lambda function.
def D(f):
    h = 0.00001
    return lambda x: (f(x+h) - f(x-h))/(2*h)

#INPUT function of single variable x, starting point x, precision tau
#OUTPUT a root of f
def newton(f,x,tau):
    while f(x) > tau:
        xn = x
        x = xn - ((f(xn))/(D(f)(xn)))
    return x


#Problem 2
#INPUT a number
#RETURN -1 if number is <= 0, 1 otherwise
def sign(x):
    if x <= 0:
        return -1
    else:
        return 1

#INPUT function, interval(a, b), tau
#RETURN root
def bisection(f,a,b,tau):
    while True:
        c = (a+b)/2
        if (b-c) <= tau:
            return c
        if sign(f(a)) == sign(f(c)):
            a = c
        else:
            b = c



#Problem 3
#INPUT function, two starting values (x0 and x1) and tau
#RETURN root
def secant(f,x0,x1,tau):
    if abs(f(x0)-f(x1)) <= tau:
        return x0
    xn = x0 - (f(x0) * ((x1-x0)/((f(x1))-(f(x0)))))
    return secant(f,x1,xn,tau)

#Problem 4
#INPUT function, start a, end b, divisions
#RETURN area
def simpson(f,a,b,n):
    acc = 0
    d = (b-a)/n
    for i in range(n+1):
        xi = a + (i*d)
        if i == 0:
            i = a+(0*d)
            a = i
            acc += f(i)
        elif i == n:
            i = a+(n*d)
            b = i
            acc += f(i)
        elif i%2 == 0:
            acc += f(xi)*2
        else:
            acc += f(xi)*4
    return ((b-a)/(3*n)) * acc

#Problem 5
#INPUT list of objects
#RETURN list of permutations
def permutation(lst):

    def perm(llst):
    
        if len(llst) == 1:
            return [llst]

        accLst = []

        lastNum = llst[-1]
        rest = llst[:-1]

        for permu in perm(rest):
            for i in range(len(permu)+1):
                accLst.append(permu[:i] + [lastNum] + permu[i:])
    
        return accLst

    result = perm(lst)
    return result

#Problem 6
#INPUT class 
#RETURN method reduce(self) completed to reduce fraction
class fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def reduce(self):
        gcd = .000001 #placeholder value
        if self.numerator > self.denominator:
            biggest = self.numerator
        else:
            biggest = self.denominator
        for i in range(1,biggest+1):
            if self.numerator%i == 0 and self.denominator%i == 0:
                if self.numerator/gcd > self.numerator/i:
                    gcd = i
        self.numerator = int(self.numerator/gcd)
        self.denominator = int(self.denominator/gcd)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

if __name__ == "__main__":
   ''' uncomment if needed'''
#   Problem 1
#    p1 = [[lambda x:x**2 - 2, 100],[lambda x:x**6-x-1,1.5],
#          [lambda x:x**3-(100*(x**2))-x + 100,0]]
#    tau = 0.0001

#    for f,g in p1:
#        root = newton(f,g,tau)
#        print(root,f(root))

#    Problem 2
#    print(bisection(lambda x:x**3-x-2,1.0,2.0,0.0001))
#    print(bisection(lambda x:x**6-x-1,1.0,2.0,.0001))

#    Problem 3
#    print(secant(lambda x:x**6-x-1,2.0,1.0,.0001))
#    print(secant(lambda x:x**3-x-2,1.0,2.0,0.0001))
   
#    Problem 4
#    print(simpson(lambda x: 3*(x**2)+1,0,6,2))
#    print(simpson(lambda x: (x**2),0,5,6))
#    print(simpson(lambda x: 1/x,1,11,6))
#    print(simpson(lambda x: math.sin(x),0,math.pi,10))

#    Problem 5
#    print(permutation([1,2,3]))
#    print(permutation([1,2,3,4]))

#    Problem 6
# x = fraction(2*3*4,4*3*5)
# y = fraction(2*7,7*2)
# z = fraction(13,14)
# a = fraction(13*2*7,14)
# print(x)
# print(y)
# print(z)
# print(a)