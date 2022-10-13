# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        node = root
        while node and node.left:
            next_node = node.left
            while node:
                node.left.next = node.right
                node.right.next = node.next.left if node.next else None
                node = node.next
            node = next_node
        return root
