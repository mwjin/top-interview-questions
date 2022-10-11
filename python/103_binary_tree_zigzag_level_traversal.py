from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        nodes = [root]
        leftFirst = True

        while nodes:
            nodes = nodes[::-1]
            values = [node.val for node in nodes]
            result.append(values)

            nodesNextLevel = []

            if leftFirst:
                for node in nodes:
                    if node.left:
                        nodesNextLevel.append(node.left)
                    if node.right:
                        nodesNextLevel.append(node.right)
            else:
                for node in nodes:
                    if node.right:
                        nodesNextLevel.append(node.right)
                    if node.left:
                        nodesNextLevel.append(node.left)

            nodes = nodesNextLevel
            leftFirst = not leftFirst

        return result
