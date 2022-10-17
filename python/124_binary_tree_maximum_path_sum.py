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
        result = root.val

        leftSum = self.calcPathSum(root.left)
        if leftSum > 0:
            result += leftSum

        rightSum = self.calcPathSum(root.right)
        if rightSum > 0:
            result += rightSum

        self.maxSum = max(result, self.maxSum)
        result -= max(0, min(leftSum, rightSum))
        return result
