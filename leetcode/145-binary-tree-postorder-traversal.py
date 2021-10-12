# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        For both iterate & recursive approaches:
            TC: O(N), N: number of nodes
            SC: O(N), N: number of nodes
    """ 
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        ret = []
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            traverse(node.right)
            ret.append(node.val)
        
        traverse(root)
        return ret
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        ret = []
        if not root:
            return ret

        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            node = stack2.pop()
            ret.append(node.val)
        
        return ret

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        ret = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ret.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return ret

