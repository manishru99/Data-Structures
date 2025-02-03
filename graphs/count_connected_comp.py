def count_connected_components(n, edges):
    # Create an adjacency list
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Function to perform DFS and mark visited nodes
    def dfs(node, visited):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    
    # Initialize visited array
    visited = [False] * n
    connected_components = 0
    
    # Count connected components using DFS
    for i in range(n):
        if not visited[i]:
            connected_components += 1
            visited[i] = True
            dfs(i, visited)
    
    return connected_components

# Example usage
n = 3
edges = [[0,1], [0,2]]
print(f"The total number of connected components in the graph is {count_connected_components(n, edges)}.")
