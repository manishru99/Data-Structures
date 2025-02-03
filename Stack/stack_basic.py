# simple implementation of a stack using a list 

class Stack:
    def __init__(self):
        self.stack=[]  #Linked list implementation of stack
    
    # Push an element onto the stack
    def push(self, e):
        self.stack.append(e)

    # Pop an element from the stack (removes and returns the top element)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()        # use this as it pops 
        else:
            return "Stack is empty!"
        '''
        if not self.stack:
            return -1
        return self.stack.pop()
        '''
    # Peek at the top element of the stack (without removing it)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"
        
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Get the size of the stack
    def size(self):
        return len(self.stack)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element is:", stack.peek())  # Output: Top element is: 30
print("Popped element is:", stack.pop())  # Output: Popped element is: 30
print("Top element after pop:", stack.peek())  # Output: Top element after pop: 20
print("Stack size is:", stack.size())  # Output: Stack size is: 2
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

'''
TC
push(element): Adding an element to the end of the list (stack) takes constant time O(1).
pop(): Removing the last element from the list (stack) also takes constant time O(1).
peek(): Accessing the top element without removing it is also a constant time operation O(1).
'''