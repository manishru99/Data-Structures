#New version

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    # Push an element onto the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top  # Point new node to the current top
        self.top = new_node  # Make the new node the top of the stack
        self.size += 1
        print(f"Pushed {value} onto the stack.")
    
    # Pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_value = self.top.value
        self.top = self.top.next  # Move the top pointer to the next node
        self.size -= 1
        print(f"Popped {popped_value} from the stack.")
        return popped_value
    
    # Peek at the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top of the stack is {self.top.value}")
        return self.top.value
    
    # Check if the stack is empty
    def is_empty(self):
        return self.top is None
    
    # Get the size of the stack
    def get_size(self):
        return self.size
    
    # Print the entire stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        stack_elements = []
        while current:
            stack_elements.append(current.value)
            current = current.next
        print("Stack:", " -> ".join(map(str, stack_elements)))

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()    # Output: Stack: 30 -> 20 -> 10
stack.peek()       # Output: Top of the stack is 30
stack.pop()        # Output: Popped 30 from the stack
stack.display()    # Output: Stack: 20 -> 10
stack.pop()        # Output: Popped 20 from the stack
stack.pop()        # Output: Popped 10 from the stack
stack.pop()        # Output: Stack is empty. Cannot pop.

'''
TC
push()	O(1)
pop()	O(1)
peek()	O(1)
is_empty()	O(1)
get_size()	O(1)
display()	O(n)
'''




























'''
#old version
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class Stack:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        current = self.head.next  # Start from the node after the dummy head node
        out = "" #Initializes an empty string out to store the string representation
        while current:
            out += str(current.value) + "->" # Append the currentrent node's value to the output string
            current = current.next # Move to the next node
        return out[:-2] # Remove the last arrow symbol "->" from the final output
        
    # Get the currentrent size of the stack
    def getSize(self):
        return self.size
    
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
    
    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we are peeking an empty stack
        if(self.isEmpty()):
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size +=1

    # Remove a value from the stack and return
    def pop(self):
        if(self.isEmpty()):
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
    
# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1,6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")

'''