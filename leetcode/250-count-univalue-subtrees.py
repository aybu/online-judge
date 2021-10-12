# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        TC: O(N), N: number of nodes
        SC: O(N), N: number of nodes
    """
    def countUnivalSubtrees(self, root):
        self.cnt_uni_tree = 0
        
        def traverse(node, parent):
            if not node:
                return True

            is_ltree_uni = traverse(node.left, node.val)
            is_rtree_uni = traverse(node.right, node.val)
            if is_ltree_uni and is_rtree_uni:
                self.cnt_uni_tree += 1
            
            return is_ltree_uni and is_rtree_uni and node.val == parent
        
        traverse(root, None)
        return self.cnt_uni_tree

