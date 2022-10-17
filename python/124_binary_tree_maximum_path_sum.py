from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        self.calcPathSum(root)
        return self.maxSum

    def calcPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        gainOnLeft = max(self.calcPathSum(root.left), 0)
        gainOnRight = max(self.calcPathSum(root.right), 0)
        self.maxSum = max(root.val + gainOnLeft + gainOnRight, self.maxSum)
        return root.val + max(gainOnLeft, gainOnRight)
