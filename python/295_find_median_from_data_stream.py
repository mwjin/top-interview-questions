import heapq


class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if self.right and self.right[0] < num:
                heapq.heappush(self.left, -heapq.heappop(self.right))
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
        else:
            if -self.left[0] > num:
                heapq.heappush(self.right, -heapq.heappop(self.left))
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -float(self.left[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
# obj.addNum(5)
print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())
