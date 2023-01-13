import random


class RandomizedSet:
    def __init__(self):
        self._set = set()
        self._list = []
        self._changed = False

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        self._set.add(val)
        self._changed = True
        return True

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            self._changed = True
            return True
        return False

    def getRandom(self) -> int:
        if self._changed:
            self._list.clear()
            self._list.extend(self._set)
            self._changed = False
        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
