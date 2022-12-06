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

        def traverseInorder(root: Optional[TreeNode]):
            if not root:
                return

            traverseInorder(root.left)
            stack.append(root.val)
            traverseInorder(root.right)

        traverseInorder(root)
        return stack[k - 1]
