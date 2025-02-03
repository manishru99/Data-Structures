class Solution:
    def inorderTraversal(self, root):
        stack = []
        inorder = []
        node = root

        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                inorder.append(node.val)
                node = node.right

        return inorder



