from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            TC: O(H), H:tree height, average case is O(logN)
            SC: O(H), H:tree height, average case is O(logN)
        """
        if not root:
            return None

        if root.val == key:
            # only left subtree exists
            if not root.left:
                return root.right

            # only right subtree exists
            if not root.right:
                return root.left

            # both left and right exist -> find smallest in the right 
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root


