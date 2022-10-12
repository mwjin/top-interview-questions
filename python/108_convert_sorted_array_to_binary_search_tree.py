from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.sortedArrayToBSTHelper(0, len(nums))

    def sortedArrayToBSTHelper(
        self, low: int, high: int
    ) -> Optional[TreeNode]:
        if low == high:
            return None
        mid = low + (high - low) // 2
        return TreeNode(
            self.nums[mid],
            self.sortedArrayToBSTHelper(low, mid),
            self.sortedArrayToBSTHelper(mid + 1, high),
        )
