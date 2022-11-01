from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = slow.next

        while fast and slow != fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next

        return False if fast is None else True
