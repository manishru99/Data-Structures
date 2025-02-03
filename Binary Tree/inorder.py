'''
Inorder: left -> root -> right
'''
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def inorder(root, arr):
    #If curr node is None
    #Base case for recursion
    if root is None:
        return
    #Recursively traverse the left subtree
    inorder(root.left, arr)
    #Append the current node's val to the list
    arr.append(root.data)
    #Recursively traverse the right subtree
    inorder(root.right, arr)

# Function to initiate inorder traversal
# and return the resulting list
def in_order(root):
    # Create an empty list to
    # store inorder traversal values
    arr = []
    # Call the inorder traversal function
    inorder(root, arr)
    # Return the resulting list
    # containing inorder traversal values
    return arr

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting inorder traversal
    result = in_order(root)

    # Displaying the inorder traversal result
    print("Inorder Traversal:", end=" ")
    # Output each value in the
    # inorder traversal result
    for val in result:
        print(val, end=" ")
    print()


'''
TC: O(N) where N is the number of nodes in the binary tree as each node of the binary tree is visited exactly once.

SC: O(N) where N is the number of nodes in the binary tree. This is because the recursive stack uses an auxiliary 
space which can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), 
consuming space proportional to the number of nodes.In the average case or for a balanced tree, the maximum number of 
nodes that could be in the stack at any given time would be roughly the height of the tree hence O(log2N).
'''