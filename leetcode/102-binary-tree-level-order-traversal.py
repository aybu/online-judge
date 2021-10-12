from typing import Optional, List

#Definition for a binary tree node.
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        def traverse(node, level):
            if not node:
                return 
            
            if len(ret) == level:
                ret.append([])
            
            ret[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return ret
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root: 
            return ret

        queue = deque([root])
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(level)
        return ret

