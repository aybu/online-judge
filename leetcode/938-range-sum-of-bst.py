from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.traverse(root, low, high)
        return self.ans

    def traverse(self, node, low, high):
        if not node:
            return 0

        if low <= node.val <= high:
            self.ans += node.val

        if low < node.val:
            self.traverse(node.left, low, high)

        if high > node.val:
            self.traverse(node.right, low, high)

