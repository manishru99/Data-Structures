def create_adjacency_list(V, edges):
    # Initialize an empty adjacency list
    adj_list = [[] for _ in range(V)]
    
    # Populate the adjacency list with edges
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)

    #return adj_list

    #modify code to return 'node:adjacency list'
    # Create a dictionary to return the output as 'node: adjacency list'
    adj_dict = {i: adj_list[i] for i in range(V)}
    return adj_dict
    

# Input values
V = 5
E = 7
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]

# Create the adjacency list
#adj_list = create_adjacency_list(V, edges)

adj_dict = create_adjacency_list(V, edges)

# Output the adjacency list
#print(adj_list)

for node, adj in adj_dict.items():
    print(f"{node}: {adj}")