# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        targets = {p.val, q.val}
        ancestors = set()

        stack = []
        visit_cnt = defaultdict(int)
        curr = root

        while stack or curr:
            if curr:
                if curr.val in targets:
                    if ancestors:
                        break
                    else:
                        ancestors = {node.val for node in stack}
                        ancestors.add(curr.val)
                        targets.remove(curr.val)

                visit_cnt[curr.val] += 1
                if visit_cnt[curr.val] == 1:
                    stack.append(curr)
                    curr = curr.left
                elif visit_cnt[curr.val] == 2:
                    curr = curr.right
                else:
                    stack.pop()
                    curr = stack[-1] if stack else None
            else:
                curr = stack[-1]

        while stack:
            top = stack.pop()
            if top.val in ancestors:
                return top
