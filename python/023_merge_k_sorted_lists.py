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
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
            root = head = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    head.next, list1 = list1, list1.next
                else:
                    head.next, list2 = list2, list2.next
                head = head.next

            remain = list1 if list1 else list2
            head.next = remain
            return root.next

        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            return mergeTwoLists(
                self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
            )
