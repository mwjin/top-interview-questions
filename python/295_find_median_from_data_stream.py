from collections import defaultdict


class MedianFinder:
    def __init__(self):
        self._buckets = defaultdict(list)
        self._bucket_size = 10000
        self._min = -100000
        self._max = 100000
        self._total_size = 0

    def addNum(self, num: int) -> None:
        self._buckets[num // self._bucket_size].append(num)
        self._total_size += 1

    def findMedian(self) -> float:
        if self._total_size == 1:
            for _, nums in self._buckets.items():
                if nums:
                    return nums[0]

        median_key = self._min // self._bucket_size
        count = len(self._buckets[median_key])
        median_num = (
            self._total_size // 2 + 1
            if self._total_size % 2
            else self._total_size // 2
        )

        while count < median_num:
            median_key += 1
            count += len(self._buckets[median_key])

        self._buckets[median_key].sort()
        median_idx = len(self._buckets[median_key]) - (count - median_num) - 1
        if self._total_size % 2:
            return float(self._buckets[median_key][median_idx])
        else:
            left = self._buckets[median_key][median_idx]
            if median_idx + 1 < len(self._buckets[median_key]):
                right = self._buckets[median_key][median_idx + 1]
            else:
                median_key += 1
                while not self._buckets[median_key]:
                    median_key += 1
                right = min(self._buckets[median_key])
            return (left + right) / 2


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
