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
            values = []
            nodesNextLevel = []

            for node in reversed(nodes):
                values.append(node.val)
                if leftFirst:
                    if node.left:
                        nodesNextLevel.append(node.left)
                    if node.right:
                        nodesNextLevel.append(node.right)
                else:
                    if node.right:
                        nodesNextLevel.append(node.right)
                    if node.left:
                        nodesNextLevel.append(node.left)

            result.append(values)
            nodes = nodesNextLevel
            leftFirst = not leftFirst

        return result
