########
########
# Write you code for midterm problems in this file.
# Do not change the name of this file.
########

# Your functions goes here

def f(xlst,n):
    newLst = [] #new list to put all the lists that are > n in
    for i in xlst:
        if len(i) > n:
            newLst.append(i)
            
    return newLst

def gravity(m1,m2,d):
    g = 6.67*(10**-11) #gravity constant
    
    forceOfGravity = (g*m1*m2)/(d**2)

    return forceOfGravity







if __name__ == "__main__":

	"""
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    Please comment the print statements before submitting your 
    final version.
	"""

#problem 1

# xlst = [[1,2,3],[1,2],[1,2,3,4],[1]]
# print(f(xlst,1))
# print(f(xlst,3))

# xlst = [[],[1,2],[1,2,3,4],[1,2,3,4,5,6]]
# print(f(xlst,0))
# print(f(xlst,2))

#problem 2

# m1,m2,d = 1,6e24,6.4e6
# print(gravity(m1,m2,d))
# 
# m1,m2,d = 1,5,6
# print(gravity(m1,m2,d))




