#_push function to insert elements of array to stack
def _push(arr):
    stack = list()
    for x in range(len(arr)):
        stack.append(arr[x])
    return stack
    

#_pop function to print elements of the stack remove as well
def _pop(stack):
    while len(stack)>0:
        print(stack.pop(), end=" ")
