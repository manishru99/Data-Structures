# Class Queue to represent a queue
class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity-1
        self.Q = [None]*capacity
        self.capacity = capacity
        #[None]*capacity: This creates a list in Python containing None elements, and the length of this list is determined by capacity.

        #[None] creates a list containing a single element None.

        #[None]*capacity then multiplies this list by capacity, resulting in a list of capacity elements, each initialized with the value None.
        #self.Q: This represents the attribute of the Queue class that holds the elements of the queue.

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity
    
    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0
    
    '''
    
    In Python, self is a convention used to represent the instance of the class within a method. When defining a class method in Python, self is the first parameter of instance methods and refers to the instance of the class itself.
    self within the isEmpty() method refers to the specific instance of the Queue class on which the method is being called.

    When you create an object of the Queue class (for example, queue = Queue(30)), methods like isEmpty() are invoked on that specific instance (queue.isEmpty()).

    Inside the isEmpty() method, self allows access to the attributes and other methods of the specific Queue instance where isEmpty() is called. For instance, self.size refers to the size attribute of that particular Queue instance.

    In summary, self is a reference to the instance of the class itself, allowing methods to access and manipulate the instance's attributes and behavior.
    '''

    # Function to add an item to the queue. 
    # It changes rear and size
    def EnQueue(self, item):
        if(self.isFull()):
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" %str(item))

    
    # Function to remove an item from queue. 
    # It changes front and size
    def DeQueue(self):
        if(self.isEmpty()):
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) %(self.capacity)
        self.size = self.size - 1

    # Function to get front of queue
    def que_front(self):
        if(self.isEmpty()):
            print("Queue is empty")
        print("Rear item is:", self.Q[self.front])

    def que_rear(self):
        if(self.isEmpty()):
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])

# Driver Code
if __name__ == '__main__':
 
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
        
    


