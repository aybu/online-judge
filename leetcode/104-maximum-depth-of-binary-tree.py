from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        TC: O(N), N: number of nodes
        SC: O(logN), N: number of nodes, the worst case could be O(N)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node:
                return 0
            return max(traverse(node.left), traverse(node.right)) + 1
        
        return traverse(root)

