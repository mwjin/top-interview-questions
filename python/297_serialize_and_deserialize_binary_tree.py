from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        values = []
        nodes = deque([root])

        while nodes:
            node = nodes.popleft()
            values.append(str(node.val) if node else "n")
            if node:
                nodes.append(node.left)
                nodes.append(node.right)

        return ",".join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        create_node = (
            lambda value: TreeNode(int(value)) if value != "n" else None
        )
        values = data.split(",")
        nodes = [create_node(values[0])]
        value_idx = 1
        node_idx = 0

        while value_idx < len(values):
            left = create_node(values[value_idx])
            nodes[node_idx].left = left
            if left:
                nodes.append(left)
            value_idx += 1

            right = create_node(values[value_idx])
            nodes[node_idx].right = right
            if right:
                nodes.append(right)
            value_idx += 1

            node_idx += 1

        return nodes[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
