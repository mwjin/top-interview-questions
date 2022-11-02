from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        walker = head.next
        runner = head.next.next

        while runner and runner.next:
            prev, walker = walker, walker.next
            runner = runner.next.next

        prev.next = None
        return self.mergeLists(self.sortList(head), self.sortList(walker))

    def mergeLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        root = ListNode()
        head = root

        while head1 and head2:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next

        head.next = head1 if head1 else head2
        return root.next
