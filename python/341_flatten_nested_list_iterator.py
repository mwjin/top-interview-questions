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
        self.stack = [[0, nestedList]]
        self.prepareStack()

    def next(self) -> int:
        result = self.topStackElem().getInteger()

        if self.stack[-1][0] == len(self.stack[-1][1]) - 1:
            self.stack.pop()
        else:
            self.stack[-1][0] += 1

        self.prepareStack()
        return result

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def topStackElem(self) -> NestedInteger:
        return self.stack[-1][1][self.stack[-1][0]]

    def prepareStack(self):
        while self.stack and not self.topStackElem().isInteger():
            nextList = self.topStackElem().getList()

            if self.stack[-1][0] == len(self.stack[-1][1]) - 1:
                self.stack.pop()
            else:
                self.stack[-1][0] += 1

            if len(nextList) > 0:
                self.stack.append([0, nextList])


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
