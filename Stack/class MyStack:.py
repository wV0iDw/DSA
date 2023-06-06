class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if self.arr:
            l = self.arr.pop()
            return l
        else:
            return -1
        #add code here