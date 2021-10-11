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
        SC: O(N), N: number of nodes
    """
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0
            
            left_path = traverse(node.left)
            right_path = traverse(node.right)
            self.diameter = max(self.diameter, left_path + right_path)
        
            # add 1 as the edge conneting it with its parent
            return max(left_path, right_path) + 1

        traverse(root)
        return self.diameter



tree = (
    TreeNode(1,
        TreeNode(2,
            TreeNode(4),
            TreeNode(5),
        ),
        TreeNode(3),
    )
)

s = Solution()
print(s.diameterOfBinaryTree(tree)) #3

tree = (
    TreeNode(1,
        TreeNode(2),
    )
)
s = Solution()
print(s.diameterOfBinaryTree(tree)) #1

