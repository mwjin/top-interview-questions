class MedianFinder:
    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        self._nums.append(num)

    def findMedian(self) -> float:
        self._nums.sort()
        l = len(self._nums)
        if l % 2 == 1:
            return float(self._nums[l // 2])
        else:
            return (self._nums[l // 2 - 1] + self._nums[l // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
