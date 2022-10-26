# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        root = head

        random_idx_table = {}
        idx = 0
        while head:
            random_idx_table[id(head)] = idx
            head = head.next
            idx += 1

        nodes = []
        nodes.append(Node(root.val))
        head = root.next
        while head:
            node = Node(head.val)
            nodes[-1].next = node
            nodes.append(node)
            head = head.next

        head = root
        idx = 0
        while head:
            if head.random:
                random_idx = random_idx_table[id(head.random)]
                nodes[idx].random = nodes[random_idx]
            head = head.next
            idx += 1

        return nodes[0]
