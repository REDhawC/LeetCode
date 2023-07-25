#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#


# @lc code=start

from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.isWord = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()


class Solution:
    def findWords(self, board, words):
        def dfs(row, col, node, path):
            if not (0 <= row <= rowLen - 1 and 0 <= col <= colLen - 1) or (
                board[row][col] == "#"
            ):  # overpass the border or this block is visited
                return

            char = board[row][col]
            child = node.children.get(char)
            if not child:
                return
            if child.isWord:
                resSet.add(path + char)
            if not child.children:
                return

            board[row][col] = "#"  # mark as visited
            for r, c in [
                (row - 1, col),
                (row + 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                dfs(r, c, child, path + char)

            board[row][col] = char  # recover block

        trie = Trie()
        resSet = set()
        for word in words:
            curNode = trie.root
            for char in word:
                curNode = curNode.children[char]
            curNode.isWord = True

        rowLen = len(board)
        colLen = len(board[0])
        for row in range(rowLen):
            for col in range(colLen):
                dfs(row, col, trie.root, "")

        resList = list(resSet)
        return resList


# a1 = [
#     ["o", "a", "a", "n"],
#     ["e", "t", "a", "e"],
#     ["i", "h", "k", "r"],
#     ["i", "f", "l", "v"],
# ]
# a2 = ["oath", "pea", "eat", "rain"]

# Solution.findWords(Solution, a1, a2)


# @lc code=end
