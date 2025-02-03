#Preorder: root -> left -> right
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def preorder(root, arr):
    #Base case
    #If curr node is None
    if root is None:
        return
    arr.append(root.data)
    preorder(root.left, arr)  #recursive call
    preorder(root.right, arr)
    
def pre_order(root):
    arr = []
    preorder(root, arr)
    return arr

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting preorder traversal
    result = pre_order(root)

    print("Preorder traversal: ",end='')
    for val in result:
        print(val, end='')
        print()


#TC = O(n)
#SC = O(n)