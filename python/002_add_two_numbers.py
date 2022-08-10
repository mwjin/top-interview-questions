from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1Head = l1
        l2Head = l2
        root = head = ListNode()
        carry = 0

        while l1Head and l2Head:
            sum = l1Head.val + l2Head.val + carry
            carry = sum // 10
            head.next = ListNode(sum % 10)
            head, l1Head, l2Head = head.next, l1Head.next, l2Head.next

        l = l1Head if l1Head else l2Head
        while l:
            sum = l.val + carry
            head.next = ListNode(sum % 10)
            carry = sum // 10
            l, head = l.next, head.next

        if carry:
            head.next = ListNode(carry)

        return root.next
