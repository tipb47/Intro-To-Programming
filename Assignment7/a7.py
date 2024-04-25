## Write the name of your programming partner below
# partner name: _________________

import os

###############
# PROBLEM ONE
###############

#choice
# You can choose this function to complete B()
def C(n, k):
    if k == 0 or k == m:
        return 1
    else:
        return C(n-1, k) + C(n-1, k-1)

#Input: a number n
#Return: The output of B as per HW instructions
def B(n):
    pass
        
 

###############
# PROBLEM TWO
###############

#Input: a number n
#Return: The output of a() as per HW instructions
def a(n):
    pass

#Input: a number n
#Return: The output using while loop
def aw(n):
    pass

#Input: generator don't need to have any input. Instead, you can set the base case values and then
# use 'yield' keyword inside a loop
#Return: The output via using generators
def a_gen():
    pass

#Input: a number n
#Return: The output using tail recursion
def at(n, v0=2, v1=3, v2=5):
    pass

#Input: a number x
#Return: The output of bb() as per HW instructions
def bb(x):
    pass 

#Input: a number x
#Return: The output using while loop
def bbw(x):
    pass

#Input: generator don't need to have any input. Instead, you can set the base case values and then
# use 'yield' keyword inside a loop
#Return: The output via using generators
def bb_gen():
    pass

#Input: a number n
#Return: The output using tail recursion
def bbt(x,v0=2,v1=-3):
    pass

#Input: numbers n, m ,p
#Return: The output of F() as per HW instructions
def F(n,m,p):
    pass

#Input: a number n, m ,p
#Return: The output using tail recursion
def Ft(n,m,p,v = 100):
    pass

#Input: a number n, m, p
#Return: The output using while loop
def Fw(n,m,p):
    pass 


def m(x,y):
    if x <= 0 and y <= 0:
        return 3
    elif x <= 0:
        return 2
    elif y <= 0:
        return 1
    else:
        return m(x-1,y-1) + m(x-1,y-2)

# Input: numbers x and y
# Return: The output using while loop 
def mw(x,y):
    pass

###############
# PROBLEM THREE
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#INPUT takes path + filename (I am using a txt file)
#RETURN returns list of tuples [(year,population),...], stick to the format of return values.
def get_data(path,name):
    pass

# Input: a year
# Return: the estimate of population for that year
def pop(year):
    pass

# Input: data
# Return: the average error as per equation 18.
def error(data):
    pass


###############
# PROBLEM four
###############
#You cannot simply divide or use modulus
#You must implement the algorithm as described
#INPUT a number n 
#RETURN True if dvisible by 11, False if not.
def div_11(n):
    pass


###############
# PROBLEM five
###############
# INPUT list of numbers
# RETURN list of nesting level and sum at that level
def sl(lst,p=0):
   pass

#PROBLEM 6
# Uncomment the following code after finishing the population problem
# Please remember to comment it back before submitting to the Autograder
# We will mnaually run the code to see if the code correctly draws the trainagles.
# import pygame, sys
# import math
# from pygame.locals import *
# import random as rn
# pygame.init()

# BLUE = (0,0,255)
# WHITE = (255,255,255)
# BLACK = (0,0,0)

# DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)

# pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
# def triangle(loc,width):
#     x,y = loc
#     z = math.sqrt(width**2 - (width/2))
#     return (x,y),(x - width/2,y + z),(x + width/2, y + z)

# DISPLAYSURF.fill(BLACK)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
# def draw_triangle(loc, w):
#     pygame.draw.polygon(DISPLAYSURF, (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255)) , (triangle(loc,w)),1)


#INPUT location and width
#RETURN nothing -- follows algorithm
#Draw the three smaller triangles as described
#in the text
# def s(loc,width):
#     if width > 1:
#         x,y = loc
#         z = math.sqrt(width**2 - (width/2))
#         draw_triangle(loc,width)
#     else:
#         return


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    # """

    #PROBLEM 1
    
    # for i in range(6):
    #     print("B({0}) = {1}".format(i,B(i)))

    #PROBLEM 2
    # for i,j in zip(range(10),a_gen()):
    #     print(f"a({i}) {a(i)} {aw(i)} {at(i)} {j} \n",end="")   
    # for i,j in zip(range(10),bb_gen()):
    #     print(f"b({i}) {bb(i)} {bbw(i)} {bbt(i)} {j}")    
    # for i in range(6):
    #     for j in range(6):
    #         for k in range(6):
    #             print(f"{i,j,k} {F(i,j,k)} {Ft(i,j,k)} {Fw(i,j,k)}")
    # for i in range(10):
    #     for j in range(10):
    #         print(f"{i,j} {m(i,j)} {mw(i,j)} ")

    #Problem 3
    # data = get_data(".", "pop.txt")
    # print(f"data from file:",data)
    # print(f"abs(3040 - {pop(60)}) = {abs(3040 - pop(60))}")
    # ave_error = round(error(data),2)
    # print(f"Average error: {ave_error}")

    # #uncomment to see plot
    # Please comment it back after you are done
    # completing the functions, otherwise the Autograder will
    # return with error.
    
    # t = np.arange(0.0, 120.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, pop(t),'g')
    # for y,p in data:
    #     ax.plot(y,p,'ro--')

    # ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    # title = "Population Model Average Error = {0}".format(ave_error))
    # ax.grid()
    # plt.show()

    #problem 4
    # nlst = [587657752,11,22,2728,31415,1358016]
    # for n in nlst:
    #     print(div_11(n), n / 11)

    #problem 5
    # prob5 = [[1,4,[3,[100]],3,2,[1,[101,1000],5],1,[7,9]],
    #          [1,2,3,4,[10,20,30,40,[100,200,300,400]]],
    #          [[[[100,200,300,400]]],[[10,20,30,40]],1,2,3,4]]
    # for lst in prob5:
    #     print(sl(lst))

    #Problem 6
    # s((240,0),440)

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     pygame.display.update()
