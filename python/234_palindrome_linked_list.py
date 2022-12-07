from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next if fast else slow
        prev = None
        while mid:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next

        rev_head = prev
        while rev_head:
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next

        return True
