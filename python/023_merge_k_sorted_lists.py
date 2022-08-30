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
                values.append(list.val)
                list = list.next
        values.sort()

        root = head = ListNode()
        for value in values:
            head.next = ListNode(value)
            head = head.next

        return root.next
