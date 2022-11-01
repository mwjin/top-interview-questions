from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        runner = walker = head

        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True

        return False
