from heapq import heappop, heappush
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if not lists:
            return None

        values = []
        for list in lists:
            while list:
                heappush(values, list.val)
                list = list.next

        root = head = ListNode()
        while values:
            head.next = ListNode(heappop(values))
            head = head.next

        return root.next
