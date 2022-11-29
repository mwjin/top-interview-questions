from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self._nextNodes = {}
        self._word = ""

    def addNextNode(self, char: str):
        if char not in self._nextNodes:
            self._nextNodes[char] = TrieNode()

    def getNextNode(self, char) -> Optional["TrieNode"]:
        return self._nextNodes.get(char)

    def removeNode(self, char):
        del self._nextNodes[char]

    def hasNext(self) -> bool:
        return bool(self._nextNodes)

    def getWord(self):
        return self._word

    def setWord(self, word):
        self._word = word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node.addNextNode(c)
            node = node.getNextNode(c)
        node.setWord(word)

    def delete(self, word: str):
        nodes = []
        curr = self.root
        for i in range(len(word)):
            nodes.append(curr)
            curr = curr.getNextNode(word[i])

        curr.setWord("")

        for i in range(len(nodes) - 1, -1, -1):
            if not nodes[i].getNextNode(word[i]).hasNext():
                nodes[i].removeNode(word[i])


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.buildTrie(words)
        self.board = board
        self.result = []
        self.traverseBoard()
        return self.result

    def buildTrie(self, words: List[str]):
        for word in words:
            self.trie.insert(word)

    def traverseBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.dfs(i, j, self.trie.root)

    def dfs(self, row_idx: int, col_idx: int, node: TrieNode):
        c = self.board[row_idx][col_idx]

        nextNode = node.getNextNode(c)
        if not nextNode:
            return

        word = nextNode.getWord()
        if word:
            self.result.append(word)
            self.trie.delete(word)

        self.board[row_idx][col_idx] = "#"
        if row_idx > 0:
            self.dfs(row_idx - 1, col_idx, nextNode)
        if col_idx > 0:
            self.dfs(row_idx, col_idx - 1, nextNode)
        if row_idx < len(self.board) - 1:
            self.dfs(row_idx + 1, col_idx, nextNode)
        if col_idx < len(self.board[0]) - 1:
            self.dfs(row_idx, col_idx + 1, nextNode)
        self.board[row_idx][col_idx] = c


Solution().findWords(
    [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],
    ["oath", "pea", "eat", "rain", "hklf", "hf"],
)
