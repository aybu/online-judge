from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        For both iterative and recursive approaches
        TC: O(N), N: number of nodes
        SC: O(N), N: number of nodes
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def is_mirror(l_node, r_node):
            if not l_node and not r_node:
                return True
            elif not l_node or not r_node:
                return False
            elif l_node.val == r_node.val:
                return is_mirror(l_node.left, r_node.right) and is_mirror(l_node.right, r_node.left)
            else:
                return False
        
        return is_mirror(root.left, root.right)


    def isSymmetric(self, root):
        if root is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            l_node, r_node = stack.pop()
            if not l_node and not r_node:
                continue
            elif not l_node or not r_node:
                return False
            elif l_node.val == r_node.val:
                stack.append((l_node.left, r_node.right))
                stack.append((l_node.right, r_node.left))
            else:
                return False
        return True

