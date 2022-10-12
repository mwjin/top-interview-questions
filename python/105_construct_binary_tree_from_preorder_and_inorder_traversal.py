from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None

        rootVal = preorder[0]
        inorderRootIdx = inorder.index(rootVal)
        leftInorder = inorder[:inorderRootIdx]
        rightInorder = inorder[inorderRootIdx + 1 :]
        leftPreorder = preorder[1 : 1 + inorderRootIdx]
        rightPreorder = preorder[1 + inorderRootIdx :]

        return TreeNode(
            rootVal,
            self.buildTree(leftPreorder, leftInorder),
            self.buildTree(rightPreorder, rightInorder),
        )
