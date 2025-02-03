#Double -ended queue

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque
    
    # Function to add an item to the queue
    def EnQueue(self, item):
        self.queue.append(item)  # Append item to the rear of the queue
        print(f"{item} enqueued to queue")
    
    # Function to remove an item from the queue
    def DeQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        item = self.queue.popleft()  # Remove item from the front of the queue
        print(f"{item} dequeued from queue")
    
    # Function to get the front item of the queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        print(f"Front item is: {self.queue[0]}")
    
    # Function to get the rear item of the queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        print(f"Rear item is: {self.queue[-1]}")
    
    # Function to check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    # Function to get the size of the queue
    def size(self):
        return len(self.queue)

# Driver Code
if __name__ == "__main__":
    queue = Queue()
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.que_front()
    queue.que_rear()
    queue.DeQueue()
    queue.que_front()
    print(f"Queue size: {queue.size()}")
    queue.DeQueue()
    queue.DeQueue()
    queue.DeQueue()

'''
TC
EnQueue: O(1)
DeQueue: O(1)
que_front/que_rear: O(1)
isEmpty/size: O(1)

SC = O(n)
'''