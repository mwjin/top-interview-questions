from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0
        stack = []
        curr = root
        while k > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                top = stack.pop()
                curr = top.right
                result = top.val
                k -= 1

        return result
