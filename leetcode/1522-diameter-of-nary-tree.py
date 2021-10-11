"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    """
        TC: O(N), N: number of nodes
        SC: O(N), N: number of nodes
        Similar to #543, but need to find top2 height from n sub-trees
    """
    def __init__(self):
        self.d = 0
    
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        def height(node):
            if not node:
                return 0
            
            max_h1, max_h2 = 0, 0
            for child in node.children:
                current_h = height(child)
                if current_h > max_h1:
                    max_h1, max_h2 = current_h, max_h1
                elif current_h > max_h2:
                    max_h2 = current_h
                
            self.d = max(self.d, max_h1 + max_h2)          
            return max_h1 + 1

        height(root)
        return self.d


