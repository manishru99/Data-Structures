class Stack:
    def __init__(self):
        self.stack=[]
    
    # Push an element onto the stack
    def push(self, e):
        self.stack.append(e)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0
    

def rev_str(str):
    stack = Stack()
    # Push all characters of the input string onto the stack
    for char in ip_str:
        stack.push(char)
    # Pop all characters from the stack and form the reversed string
    re_str=''
    while not stack.is_empty():
        re_str += stack.pop()
    return re_str




ip_str = input("String to be reversed: ")
op_str = rev_str(ip_str)
print(f"Reversed string: {op_str}")
