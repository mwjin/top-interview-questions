from typing import List


class MinStack:
    class Node:
        def __init__(self, val, min_val) -> None:
            self._val = val
            self._min = min_val

        @property
        def val(self):
            return self._val

        @property
        def min_val(self):
            return self._min

    def __init__(self):
        self._stack: List[self.Node] = []

    def push(self, val: int) -> None:
        min_value = min(val, self._stack[-1].min_val) if self._stack else val
        self._stack.append(self.Node(val, min_value))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1].val

    def getMin(self) -> int:
        return self._stack[-1].min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
