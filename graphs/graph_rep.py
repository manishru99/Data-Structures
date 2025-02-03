#Graph Representation
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        #n x n matrix for storing nodes
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        self.adj_list = {i: [] for i in range(vertices)}
    '''
    Adjacency Matrix:
    The graph is represented as a 2D list (matrix) where matrix[i][j] is 1 (or 
    weight) if there is an edge between vertices i and j.
    '''

    def add_edge_matrix(self, src, dest, weight=1):
        """Add an edge to the adjacency matrix."""
        self.adj_matrix[src][dest] = weight
        self.adj_matrix[dest][src] = weight #Add this line for undirected graph
    #SC = O(n**2)

    def display_matrix(self):
        """Display the adjacency matrix."""
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

    '''Adjacency List:
    The graph is represented as a dictionary, where keys are vertices and values 
    are lists of tuples representing adjacent vertices and weights.
    '''

    def add_edge_list(self, src, dest, weight = 1):
        """Add an edge to the adjacency list."""
        self.adj_list[src].append((dest, weight))
        self.adj_list[dest].append((src, weight))  # For undirected graph
    #SC = O(2xE) where E denotes the number of edges.
    
    def display_list(self):
        """Display the adjacency list."""
        print("\nAdjacency List:")
        for key, value in self.adj_list.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = Graph(5)

    # Add edges
    edges = [
        (0, 1), (0, 2), (1, 2), (1, 3), (2, 4)
    ]
    #For weighted graphs we take 3rd term as weight
    #eg. edges = [(0,1,2), (0,2,1)] 

    for src, dest in edges:
        graph.add_edge_matrix(src, dest)
        graph.add_edge_list(src, dest)
    
    # Display graph representations
    graph.display_matrix()
    graph.display_list()


#Without using class implementation
'''
def create_adjacency_matrix(vertices):
    """Create an adjacency matrix for a graph with given vertices."""
    return [[0] * vertices for _ in range(vertices)]


def create_adjacency_list(vertices):
    """Create an adjacency list for a graph with given vertices."""
    return {i: [] for i in range(vertices)}


def add_edge_matrix(matrix, src, dest, weight=1, directed=False):
    """Add an edge to the adjacency matrix."""
    matrix[src][dest] = weight
    if not directed:
        matrix[dest][src] = weight


def add_edge_list(adj_list, src, dest, weight=1, directed=False):
    """Add an edge to the adjacency list."""
    adj_list[src].append((dest, weight))
    if not directed:
        adj_list[dest].append((src, weight))


def display_matrix(matrix):
    """Display the adjacency matrix."""
    print("Adjacency Matrix:")
    for row in matrix:
        print(row)


def display_list(adj_list):
    """Display the adjacency list."""
    print("\nAdjacency List:")
    for key, value in adj_list.items():
        print(f"{key}: {value}")


# Example usage:
if __name__ == "__main__":
    # Number of vertices
    vertices = 5

    # Create graph representations
    adj_matrix = create_adjacency_matrix(vertices)
    adj_list = create_adjacency_list(vertices)

    # Define edges
    edges = [
        (0, 1), (0, 2), (1, 2), (1, 3), (2, 4)
    ]

    # Add edges
    for src, dest in edges:
        add_edge_matrix(adj_matrix, src, dest)
        add_edge_list(adj_list, src, dest)

    # Display graph representations
    display_matrix(adj_matrix)
    display_list(adj_list)
'''