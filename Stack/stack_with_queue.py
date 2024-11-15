#New approach with 2 queues
# FOr expalantion rfr chatgpt
#Making push() operation costly.

from collections import deque

class StackWithQueues:
    def __init__(self):
        self.q1 = deque()  # Main queue for holding elements
        self.q2 = deque()  # Temporary queue used for the push operation
    
    # Push operation (Costly in this approach)
    def push(self, value):
        print(f"Pushed {value} onto the stack.")
        # Step 1: Add the new element to q2
        self.q2.append(value)
        #TC = O(n)
        
        # Step 2: Transfer all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Step 3: Swap q1 and q2 so that q1 is always the main queue
        self.q1, self.q2 = self.q2, self.q1
    
    # Pop operation (Efficient in this approach)
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_value = self.q1.popleft()
        print(f"Popped {popped_value} from the stack.")
        return popped_value
    #TC = O(1)
    
    # Peek at the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top of the stack is {self.q1[0]}")
        return self.q1[0]
    #TC = O(1)

    # Check if the stack is empty
    def is_empty(self):
        return len(self.q1) == 0
    #TC = O(1)

    # Get the size of the stack
    def size(self):
        return len(self.q1)
    #TC = O(1)

    # Print the entire stack
    def display(self):
        print("Stack:", list(self.q1))

# Example usage
stack = StackWithQueues()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()    # Output: Stack: [30, 20, 10]
stack.peek()       # Output: Top of the stack is 30
stack.pop()        # Output: Popped 30 from the stack
stack.display()    # Output: Stack: [20, 10]
stack.pop()        # Output: Popped 20 from the stack
stack.pop()        # Output: Popped 10 from the stack
stack.pop()        # Output: Stack is empty. Cannot pop.




#Making pop() operation costly.
#code
'''
from collections import deque

class StackWithQueuesCostlyPop:
    def __init__(self):
        self.q1 = deque()  # Primary queue for storing elements
        self.q2 = deque()  # Secondary queue for assisting with the pop operation

    # Push operation (Efficient in this approach)
    def push(self, value):
        print(f"Pushed {value} onto the stack.")
        # Simply add the new element to q1
        self.q1.append(value)

    # Pop operation (Costly in this approach)
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        
        # Step 1: Move all elements except the last one from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Step 2: The last element left in q1 is the element to pop
        popped_value = self.q1.popleft()
        
        # Step 3: Swap q1 and q2 so that q1 again becomes the main queue
        self.q1, self.q2 = self.q2, self.q1
        
        print(f"Popped {popped_value} from the stack.")
        return popped_value
    
    # Peek at the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        
        # Similar to pop(), but we don't remove the last element
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        # Peek the last element left in q1
        top_value = self.q1.popleft()
        self.q2.append(top_value)  # Put it back to q2 to maintain the order
        
        # Swap q1 and q2 to maintain the queue state
        self.q1, self.q2 = self.q2, self.q1
        
        print(f"Top of the stack is {top_value}")
        return top_value
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.q1) == 0
    
    # Get the size of the stack
    def size(self):
        return len(self.q1)
    
    # Print the entire stack
    def display(self):
        print("Stack:", list(self.q1))

# Example usage
stack = StackWithQueuesCostlyPop()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()    # Output: Stack: [10, 20, 30]
stack.peek()       # Output: Top of the stack is 30
stack.pop()        # Output: Popped 30 from the stack
stack.display()    # Output: Stack: [10, 20]
stack.pop()        # Output: Popped 20 from the stack
stack.pop()        # Output: Popped 10 from the stack
stack.pop()        # Output: Stack is empty. Cannot pop.

'''
























'''
from queue import LifoQueue

#Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements in the stack
print(stack.qsize())
 
# put() function to push element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() function to pop element from stack in LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())
'''