#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        ans = ""
        ans_pt = ""
        s = s.split(" ")
        curInt = 0
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            curWord = s.pop()
            curChar = pattern[-(i + 1)] + "*"
            if not curChar in hashmap:
                if curWord in hashmap:
                    return False
            if not curWord in hashmap:
                if curChar in hashmap:
                    return False
                curInt += 1
                hashmap[curWord] = curInt
                hashmap[curChar] = curInt
            ans += str(hashmap[curWord])
            ans_pt += str(hashmap[curChar])
        if ans_pt == ans:
            return True
        else:
            return False


pattern = "abba"
s = "dog cat cat dog"
Solution.wordPattern(Solution, pattern, s)
# @lc code=end
