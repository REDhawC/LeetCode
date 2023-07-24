#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
import collections


class Node:
    def __init__(self) -> None:
        self.isWord = False
        self.children = collections.defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curNode = self.root
        for char in word:
            # move to the last char and mark all nodes alongside the route
            curNode = curNode.children[char]
        curNode.isWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            curNode = curNode.children.get(char)
            if not curNode:
                return False
        return curNode.isWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            curNode = curNode.children.get(char)
            if not curNode:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
