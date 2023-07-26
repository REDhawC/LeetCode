#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
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
        self.charSet = set()

    def add(self, word):
        curNode = self.root
        for char in word:
            if char not in self.charSet:
                self.charSet.add(char)
            curNode = curNode.children[char]
        curNode.isWord = True

    def search(self, word):
        curNode = self.root
        for char in word:
            if char not in self.charSet:
                return False
            if not curNode.children.get(char):
                return False
            curNode = curNode.children[char]
        return curNode.isWord


# class Solution:
#     def wordBreak(self, s, wordDict):
#         # 将单词字典转换为集合，方便后续的查找操作
#         wordSet = set(wordDict)
#         # 计算字符串 s 的长度
#         length = len(s)
#         # 用于记录每个位置是否已经被访问过
#         visited = [False] * length

#         # 创建一个队列，用于保存待访问的位置
#         queue = []
#         queue.append(0)

#         # BFS，遍历所有可能的划分方式
#         while queue:
#             # 取出队首的位置
#             start = queue.pop(0)
#             # 如果该位置已经被访问过，则跳过
#             if visited[start]:
#                 continue
#             # 标记该位置已经被访问过
#             visited[start] = True

#             # 枚举从当前位置开始的所有可能的前缀
#             for i in range(start + 1, length + 1):
#                 # 取出当前前缀
#                 prefix = s[start:i]
#                 # 如果当前前缀在单词字典中，则继续考虑剩余部分的划分
#                 if prefix in wordSet:
#                     # 如果剩余部分非空，则将剩余部分的起始位置入队
#                     if i < length:
#                         queue.append(i)
#                     # 否则说明已经划分完毕，返回 True
#                     else:
#                         return True

#         # 遍历所有可能的划分方式后仍没有返回 True，则返回 False
#         return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)

        from collections import deque

        queue = deque()
        visited = set()
        length = len(s)
        queue.append(0)
        while queue:
            size = len(queue)
            for i in range(size):
                curIdx = queue.popleft()
                if curIdx in visited:
                    continue
                visited.add(curIdx)
                for idx in range(curIdx, length + 1):
                    curStr = s[curIdx:idx]
                    if trie.search(curStr):
                        if idx < length:
                            queue.append(idx)
                        else:
                            return True

        return False


# @lc code=end
