from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        nodeSetA = set()

        while headA:
            nodeSetA.add(id(headA))
            headA = headA.next

        while headB and id(headB) not in nodeSetA:
            headB = headB.next

        return headB
