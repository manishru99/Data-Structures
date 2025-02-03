from collections import deque

# For BFS: Queue used

# BFS from given source s
def bfs(adj, s, visited):
    # Create a queue for BFS
    q = deque()

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        # Dequeue a vertex from the queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent has not been visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Function to perform BFS traversal for a disconnected graph
def bfs_disconnected(adj):
    # Number of vertices in the graph
    v = len(adj)

    # Initially mark all the vertices as not visited
    visited = [False] * v

    # Perform BFS for each component
    for i in range(v):
        if not visited[i]:
            bfs(adj, i, visited)
            print()  # Print a newline to separate components

# Example usage
if __name__ == "__main__":
    # Number of vertices in the graph
    v = 7

    # Adjacency list representation of the graph
    adj = [[] for _ in range(v)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)
    add_edge(adj, 5, 6)

    # Perform BFS traversal for the entire graph
    print("BFS traversal for the entire graph:")
    bfs_disconnected(adj)





















'''
from collections import deque

# BFS from given source s
def bfs(adj, s, visited):
    # Create a queue for BFS
    q = deque()

    # Initially mark all the vertices as not visited
    # When we push a vertex into the q, we mark it as 
    # visited
    #visited = [False] * len(adj)

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    #iterate over the queue
    while q:

        #dequeue a vertex from the queue and print it
        curr = q.popleft()
        print(curr, end = " ")

        # Get all adjacent vertices of the dequeued 
        # vertex. If an adjacent has not been visited, 
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

###########
#perform bfs for entire graph 
def disconnected(adj):
    visited = [False] * len(adj)

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited)
############


# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    v = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(v)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0)


    #TC = O(V+E)  -no of vertices+no of edges
    #SC = O(V)
    '''