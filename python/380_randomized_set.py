import random


class RandomizedSet:
    def __init__(self):
        self._num_to_idx = {}
        self._list = []
        self._changed = False

    def insert(self, val: int) -> bool:
        if val in self._num_to_idx:
            return False
        self._num_to_idx[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self._num_to_idx:
            val_idx = self._num_to_idx[val]
            self._num_to_idx[self._list[-1]] = val_idx

            del self._num_to_idx[val]

            self._list[-1], self._list[val_idx] = (
                self._list[val_idx],
                self._list[-1],
            )
            self._list.pop()

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
