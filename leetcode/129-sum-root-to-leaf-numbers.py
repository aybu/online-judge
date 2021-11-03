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
        SC: O(H), H: height of tree
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum_root_to_leaf = 0
        
        def traverse(node, cur_val):
            if not node:
                return
            
            cur_val = cur_val * 10 + node.val
            
            if node and not node.left and not node.right:
                self.sum_root_to_leaf += cur_val
            
            traverse(node.left, cur_val)
            traverse(node.right, cur_val)

            
        traverse(root, 0)
        return self.sum_root_to_leaf


