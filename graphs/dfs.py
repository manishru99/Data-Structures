#DFS using list data structure

#TC =  O(V + E)
#SC = O(V)


# Function to create an adjacency list from user input
def create_graph(num_nodes, num_edges):
    #graph = []
    graph = {}

    # Initialize graph with empty lists for each node
    for i in range(num_nodes):
        node = input(f"Enter the name of node {i+1}: ")
        graph[node] = []

    # Take input for each edge and update adjacency list
    for i in range(num_edges):
        u, v = input(f"Enter edge {i+1} (format: node1 node2): ").split()
        graph[u].append(v)  # Directed graph (u -> v)
        graph[v].append(u)  # For undirected graph, add both (u -> v) and (v -> u)

    return graph

#Recursive DFS implementation
def dfs_recursive(graph, node, visited):
    # Mark node as visited by adding to the visited list
    #For 1st time its the start node
    visited.append(node)  
    print(node, end = ' ')

    #Recur for all adjacent vertices
    for neighbor in graph[node]:
        if neighbor not in visited:        # Check if neighbor is not in the visited list
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, s):
    stack = [s] # Stack to hold nodes to visit
    visited = []  # List to track visited nodes

    while stack:          #while stack is not empty it'll run
        node = stack.pop()      # Get the last node (DFS goes deep)

        if node not in visited:
            print(node, end = ' ')   #process the node
            visited.append(node)       #mark node as visited

            #add all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):   # Reversed to maintain DFS order
                if neighbor not in visited:
                    stack.append(neighbor)


# Main function to execute the DFS algorithms
def main():
    # Take input from the user for the number of nodes and edges
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))

    # Create the graph using an adjacency list
    graph = create_graph(num_nodes, num_edges)
    
    print("\nAdjacency List Representation of Graph:")
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")

    # Take input for starting node
    start_node = input("\nEnter the starting node for DFS: ")

    # Run Recursive DFS
    print("\nDFS (Recursive):")
    visited = [] # List to keep track of visited nodes
    dfs_recursive(graph, start_node, visited)

    # Run Iterative DFS
    print("\n\nDFS (Iterative):")
    dfs_iterative(graph, start_node)

if __name__ == "__main__":
    main()