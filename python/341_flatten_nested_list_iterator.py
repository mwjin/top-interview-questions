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
        def _flattenNestedList(nestedList: List[NestedInteger]) -> List[int]:
            result = []
            for elem in nestedList:
                if elem.isInteger():
                    result.append(elem.getInteger())
                else:
                    result.extend(_flattenNestedList(elem.getList()))
            return result

        self._list = _flattenNestedList(nestedList)
        self._next_idx = 0

    def next(self) -> int:
        result = self._list[self._next_idx]
        self._next_idx += 1
        return result

    def hasNext(self) -> bool:
        return self._next_idx < len(self._list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
