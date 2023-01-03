from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_head = head
        even_head = head.next

        if not even_head:
            return head

        odd_prev, odd_curr = None, odd_head
        even_prev, even_curr = None, even_head

        while odd_curr and odd_curr.next and even_curr and even_curr.next:
            odd_prev, even_prev = odd_curr, even_curr
            odd_curr, even_curr = odd_curr.next.next, even_curr.next.next
            odd_prev.next, even_prev.next = odd_curr, even_curr

        odd_curr.next = even_head

        return head
