from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        traverse = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                top = stack.pop()
                traverse.append(top.val)
                curr = top.right

        return traverse[k - 1]
