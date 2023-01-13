import random


class RandomizedSet:
    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        self._set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self._set))  # Not O(1)!


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
