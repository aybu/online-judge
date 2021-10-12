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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        ret = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)            
            ret.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return ret
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        ret = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ret.append(node.val)
                root = node.right

        return ret

