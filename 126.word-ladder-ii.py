#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#


# @lc code=start


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        import collections

        # 定义答案
        ans = []
        # 转为set，判断是否存在快很多， 不然127题就会超时
        wordList = set(wordList)

        # 终点如果不存在于单词中，直接返回
        if endWord not in wordList:
            return ans

        # 我们下面题解中会多次用到一个单词对应的路径的最短距离：
        # 这个是指这个单词在最短路径中离beginWord或者离endWord的距离（根据方向不同，降序升序也有不同）

        # 首先先用一遍bfs去找到终点对应的路径的最短距离
        # 这里用dist记录从beginWord到某个单词的最短距离，遇到endWord就跳出
        # 这样子最后符合条件的最短路径中终点之前的单词的最短路径的距离也会被保存下来
        dist = {}
        dist[beginWord] = 0

        # BFS
        st = collections.deque()
        st.append(beginWord)

        def f():
            while st:
                q = st.popleft()
                for xx in range(len(q)):
                    for index in range(97, 123):
                        tempq = q[:xx] + chr(index) + q[xx + 1 :]
                        if tempq in wordList and tempq not in dist:
                            dist[tempq] = dist[q] + 1
                            if tempq == endWord:
                                return
                            st.append(tempq)

        f()
        # BFS end

        # 重点来了，敲黑板
        # 因为我们前面找最短长度时候，是顺着找，其实是有很多路径试错的
        # 特别是加的那个第32个测试用例，"aaaaa"，"ggggg"那个
        # 如果我们再找路径的时候还是和上面的一样顺着遍历， 我pycharm跑了好久都没跑出来， 试错路径太多了

        # 这里我们反着来， 正着找和反着找，试错的路径会有很多不一样，但是能到终点的正确的路径是会包含的
        # 为何？ 这里要体会一下，因为我们在第一步中仅仅是找到路径的长度
        # 并且！ 所有比目标矮一级的单词我们都找到了(bfs性质)

        # 第一步中找到的节点对应的长度只是所有节点的子集， 下面这里也只用到了路径的长度这一个信息

        # 从终点开始遍历， 那么越离起点进，dist里面值是越小的
        # 所以判断是dist[root] == dist[temproot] + 1:
        # 当前单词的距离 = 改一个字母的单词的距离 + 1
        path = [endWord]

        def bfs(root):
            # 遇到起点，反向，加入答案
            if root == beginWord:
                ans.append(path[::-1])
            else:
                for xx in range(len(root)):
                    for index in range(97, 123):
                        # temproot是改变了一个单词的root
                        temproot = root[:xx] + chr(index) + root[xx + 1 :]
                        # 重点来了，如果temproot的高度我们获取到了
                        # 那么最短路径是可能包含这个单词的（也可能不包含，得试）
                        # 然后如果我们下一个遍历的单词的长度是
                        if temproot in dist and dist[root] == dist[temproot] + 1:
                            path.append(temproot)
                            bfs(temproot)
                            path.pop()

        bfs(endWord)
        return ans


# class Solution:
#     def findLadders(
#         self, beginWord: str, endWord: str, wordList: list[str]
#     ) -> list[list[str]]:
#         # import copy
#         from collections import deque

#         wordSet = set(wordList)
#         if endWord not in wordSet:
#             return []
#         queue = deque()
#         visited = set()
#         beginList = list()
#         beginList.append(beginWord)
#         resList = list()
#         queue.append(beginList)
#         foundMinStep = False
#         while queue and not foundMinStep:
#             size = len(queue)
#             for idx in range(size):
#                 curList = queue.popleft()

#                 if curList[-1] == endWord:
#                     foundMinStep = True
#                     resList.append(curList)
#                 else:
#                     if curList[-1] not in visited:
#                         curWord = curList[-1]
#                         wordSet.discard(curWord)
#                         for charIndex in range(len(curWord)):
#                             # for every pos in this word,
#                             for i in range(26):
#                                 # test 26 letter in this pos
#                                 newChar = chr(ord("a") + i)
#                                 newWord = (
#                                     curWord[:charIndex]
#                                     + newChar
#                                     + curWord[charIndex + 1 :]
#                                 )
#                                 # print(newWord)
#                                 if newWord == curWord:
#                                     continue
#                                 if newWord not in wordSet:
#                                     continue
#                                 # if newWord not in visited:
#                                 #     visited.add(newWord)
#                                 newList = curList[:]
#                                 newList.append(newWord)
#                                 queue.append(newList)
#                                 # print(newList)
#         return resList


# @lc code=end
