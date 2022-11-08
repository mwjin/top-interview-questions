import heapq
from collections import defaultdict


class MinStack:
    def __init__(self):
        self._stack = []
        self._counter = defaultdict(int)
        self._minHeap = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._counter[val] += 1
        heapq.heappush(self._minHeap, val)

    def pop(self) -> None:
        self._counter[self._stack.pop()] -= 1

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        while not self._counter[self._minHeap[0]]:
            heapq.heappop(self._minHeap)
        return self._minHeap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
