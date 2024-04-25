print("------- iterative search -------")

def binarySearch(array, x, low, high): #iterative approach
    
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        
        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    
    return -1


#unit test

array = [3,4,5,6,7,8,9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print(f"Element is present at index {str(result)}")
else:
    print("not found")

print("------- recursive search -------")


def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high-low)//2

        if array[mid] == x:
            return mid

        #search left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        
        #search right half
        else:
            return binarySearch(array, x, mid+1, high)
    
    else:
        return -1

array = [3,4,5,6,7,8,9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print(f"Element is present at index {str(result)}")
else:
    print("not found")

print("------- bubble sort -------")

def bubbleSort(array):

    for i in range(len(array)):

        for j in range(0, len(array)-i-1):

            if array[j] > array[j+1]:

                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    return array

data = [-2, 45, 0, 11, -9]

print(f'bubble sorted ascending: {bubbleSort(data)}')

print("------- insertion sort -------")

def insertionSort(array):

    for step in range(1, len(array)):

        key = array[step]
        j = step - 1

        #compare key w/ each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1

            #place key at after the element just smaller than it
            array[j+1] = key

data = [-2, 45, 0, 11, -9]

print(f'insertion sorted ascending: {bubbleSort(data)}')
