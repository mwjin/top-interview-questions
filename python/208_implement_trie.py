from typing import Optional


class TrieNode:
    def __init__(self) -> None:
        self._nextNodes = [None for _ in range(ord("z") - ord("a") + 1)]
        self._isWordEnd = False

    def getNextNode(self, char) -> Optional["TrieNode"]:
        return self._nextNodes[ord(char) - ord("a")]

    def setNextNode(self, char: str, node: "TrieNode"):
        self._nextNodes[ord(char) - ord("a")] = node

    def isWordEnd(self):
        return self._isWordEnd

    def markAsEnd(self):
        self._isWordEnd = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            nextNode = node.getNextNode(c)
            if not nextNode:
                nextNode = TrieNode()
                node.setNextNode(c, nextNode)
            node = nextNode
        node.markAsEnd()

    def search(self, word: str) -> bool:
        lastNode = self._findLastNode(word)
        return lastNode and lastNode.isWordEnd()

    def startsWith(self, prefix: str) -> bool:
        return self._findLastNode(prefix) is not None

    def _findLastNode(self, word: str) -> Optional[TrieNode]:
        node = self.root
        for c in word:
            node = node.getNextNode(c)
            if not node:
                return None
        return node


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
print(param_2)
# param_3 = obj.startsWith(prefix)
