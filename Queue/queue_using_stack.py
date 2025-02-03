'''
Maintain Two stacks s1, s2
For PUSH: (push x)
s1 -> s2
x -> s1
s2 -> s1
'''
class MyQueue:
#Approach 1: push O(n), pop O(1), top O(1)
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        #s1 -> s2
        while self.s1:
            self.s2.append(self.s1.pop())
        #x -> s1
        self.s1.append(x)
        #s2 -> s1
        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#Approach 2: push O(1), pop O(n), top O(n)
#(amortized TC for pop and top is (O(1)))

'''
Algo:
push(x):
x -> s1

pop():
if s2 != empty:
    s2.pop
else:
    s1 -> s2
    s2.pop

top:
if s2 != empty:
    s2.top
else:
    s1 -> s2
    s2.top


    
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2    
'''