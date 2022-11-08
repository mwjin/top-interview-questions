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
        nodesA, nodesB = [], []

        while headA:
            nodesA.append(headA)
            headA = headA.next

        while headB:
            nodesB.append(headB)
            headB = headB.next

        result = None

        while nodesA and nodesB and nodesA[-1] == nodesB[-1]:
            result = nodesA.pop()
            nodesB.pop()

        return result
