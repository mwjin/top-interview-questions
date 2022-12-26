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
        root = create_node(values[0])
        nodes = deque([root])
        value_idx = 1

        while value_idx < len(values):
            node = nodes.popleft()
            left = create_node(values[value_idx])
            node.left = left
            if left:
                nodes.append(left)
            value_idx += 1

            right = create_node(values[value_idx])
            node.right = right
            if right:
                nodes.append(right)
            value_idx += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
