from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = [root]

        while q:
            values = []
            newQueue = []

            for node in q:
                values.append(node.val)
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)

            q = newQueue
            result.append(values)

        return result
