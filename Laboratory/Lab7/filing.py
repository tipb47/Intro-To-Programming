import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()




def readingEx1():
    with open("Lab7/blank.txt", "r") as someFile:
        someFile = open("Lab7/blank.txt", "r")
        contents = someFile.read()
        return contents
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    


def readingEx2():
    with open("Lab7/blank.txt", "r") as someFile:
        someFile = open("Lab7/blank.txt", "r")
        contents = someFile.readlines()
        return contents
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    


def writeEx1():
    stuff = ['a', 'b', 'c', 'd', 'e', 'f']
    with open("Lab7/blank.txt", "w") as fileToWrite:
        for s in stuff:
            fileToWrite.write(s + '\n')
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    pass


def writeEx2():
    with open("Lab7/blank.txt", "a") as fileToWrite:
        for s in range(4):
            fileToWrite.write("more\n")
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    



def FileIO_example(filePath, newFile): 
    acc = 0
    with open(filePath, "r") as f:
        with open(newFile, "w") as nf:
            for line in f.readlines():
                if len(line.split()) > 5:
                    nf.write(line.strip() + '\n')
                else:
                    acc += 1
    return acc
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    


def calculation(filePath):
    last = ''
    sum = 0
    with open(filePath, "r") as file:
        for i in file.readlines():
            if not last:
                last = int(i)
            else:
                sum += int(i)*last
    return sum

    '''
    Given a file path, we want to open the file, read each line. in each line we have a number
    we want to calculate the summation of numbers in last 2 lines and write the sum at the end of the 
    file we read from it. (eah time that we run this function we add one number of fibonacci series to the file)
    '''
    pass


if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example("Lab7/testing.data", "Lab7/clean.txt")))

    print(calculation("Lab7/calculation.txt"))