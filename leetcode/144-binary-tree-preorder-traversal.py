from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        For both iterate & recursive approaches:
            TC: O(N), N: number of nodes
            SC: O(N), N: number of nodes
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        ret = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return ret
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        ret = []
        def traverse(node):
            if not node:
                return
            
            ret.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return ret
 
