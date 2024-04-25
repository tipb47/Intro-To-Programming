class Stack:

    def __init__(self):
        self.stack = []
        """
        Initializes the stack as a data structure such as a list or 
        an array
        """
    

    def pop(self):
        if self.stack == []:
            return None
        else:
            return self.stack.pop()
        """
        Removes the first item from the stack.
        Implemented so that there is not an error if the start
        is empty
        """
        
    

    def push(self, item):
        self.stack.append(item)
        """
        Pushes an item on to a stack
        """

    

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

        """
        Returns True is stack is empty, False otherwise
        """
    
    def peek(self):
        return self.stack[len(self.stack)-1]
        """
        Shows what the first item on the stack is. Will keep the stack
        the same, since you just want to see what the value is.
        Returns the item on the top of te stack
        """
    
    def __str__(self):
        pass