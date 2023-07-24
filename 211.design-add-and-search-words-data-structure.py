#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
import collections


class Node:
    def __init__(self) -> None:
        self.isWord = False
        self.children = collections.defaultdict(Node)


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curNode, curNode_Any = self.root, self.root

        def add(node, remainingWord):
            for char in remainingWord:
                node = node.children[char]
            node.isWord = True

        for idx in range(len(word)):
            char = word[idx]
            curNode = curNode.children[char]
            if idx > 0:
                remainingWord = word[idx:]
                remainingWordList=[]
                for idx in range(len(remainingWord)):
                    # pass... more
                tempAny = curNode_Any
                add(tempAny, remainingWord)

            curNode_Any = curNode_Any.children["."]
        curNode.isWord, curNode_Any.isWord = True, True

    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            curNode = curNode.children.get(char)
            if not curNode:
                return False
        return curNode.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
