#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import collections

        queue = collections.deque()
        visited = set()
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue.append((beginWord, 0))
        while queue:
            curWord, step = queue.popleft()
            # print(curWord, type(curWord))
            if curWord == endWord:
                # for i in visited:
                #     print(i)
                # print(len(visited))
                return step + 1
            for char_Index in range(len(curWord)):
                for i in range(26):
                    newChar = chr(ord("a") + i)
                    # print(newChar)
                    newWord = curWord[:char_Index] + newChar + curWord[char_Index + 1 :]
                    # print(newWord, curWord)
                    if newWord == curWord:
                        continue
                    if newWord not in wordSet:
                        continue
                    if newWord not in visited:
                        # print(newWord)
                        visited.add(newWord)
                        queue.append((newWord, step + 1))

        return 0


# @lc code=end
