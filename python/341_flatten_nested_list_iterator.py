from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedInteger:
    pass


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self._next_idx = 0
        self._list = []

        stack = [[0, nestedList]]
        while stack:
            idx, aList = stack.pop()
            while idx < len(aList) and aList[idx].isInteger():
                self._list.append(aList[idx].getInteger())
                idx += 1

            if idx < len(aList):
                stack.append([idx + 1, aList])
                stack.append([0, aList[idx].getList()])

    def next(self) -> int:
        result = self._list[self._next_idx]
        self._next_idx += 1
        return result

    def hasNext(self) -> bool:
        return self._next_idx < len(self._list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
