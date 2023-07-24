#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
import collections


class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(word, 0, self.root)

    def match(self, word, index, root):
        if root == None:
            return False
        if index == len(word):
            return root.isword
        if word[index] != ".":
            return root != None and self.match(
                word, index + 1, root.children.get(word[index])
            )
        else:
            for child in root.children.values():
                if self.match(word, index + 1, child):
                    return True
        return False


# class Node:
#     def __init__(self) -> None:
#         self.isWord = False
#         self.children = collections.defaultdict(Node)


# class WordDictionary:
#     def __init__(self):
#         self.root = Node()

#     def addWord(self, word: str) -> None:
#         dummy = self.root
#         level = 0

#         def add(node, word, level):
#             if level == len(word):
#                 node.isWord = True
#                 return

#             temp = node
#             char = word[level]
#             # print(word)
#             for i in "." + char:
#                 # print(level, i)
#                 curNode = temp.children[i]
#                 add(curNode, word, level + 1)

#         add(dummy, word, level)

#     def search(self, word: str) -> bool:
#         curNode = self.root
#         for char in word:
#             curNode = curNode.children.get(char)
#             if not curNode:
#                 return False
#         return curNode.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
