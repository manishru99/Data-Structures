#Postorder: left -> right -> root
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def postorder(root, arr):
    #Base case
    #If curr node is None
    if root is None:
        return
    
    postorder(root.left, arr)
    postorder(root.right, arr)
    arr.append(root.data)
    
def post_order(root):
    arr = []
    postorder(root, arr)
    return arr

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting preorder traversal
    result = post_order(root)

    print("Postorder traversal: ",end='')
    for val in result:
        print(val, end='')
        print()