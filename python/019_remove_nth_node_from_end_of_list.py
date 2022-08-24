from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        root = ListNode(0, head)
        fastRunner = slowRunner = root

        while n > 0 and fastRunner.next is not None:
            fastRunner = fastRunner.next
            n -= 1

        while fastRunner.next is not None:
            slowRunner = slowRunner.next
            fastRunner = fastRunner.next

        slowRunner.next = slowRunner.next.next

        return root.next
