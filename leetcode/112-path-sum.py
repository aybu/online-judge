from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        For both iterative and recursive approaches:
        TC: O(N)
        SC: O(N)
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node, cur_sum):
            if not node:
                return
            
            # check if node is leaf
            if node and not node.left and not node.right:
                return cur_sum == node.val
            return traverse(node.left, cur_sum - node.val) or traverse(node.right, cur_sum - node.val)

        return traverse(root, targetSum)
    

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum)]
        
        while stack:
            node, cur_sum = stack.pop()
            if not node.left and not node.right and cur_sum == node.val:
                return True
            
            if node.left:
                stack.append((node.left, cur_sum - node.val))

            if node.right:
                stack.append((node.right, cur_sum - node.val))
            
        return False

