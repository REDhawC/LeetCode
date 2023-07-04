#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in s:
            if not i in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in t:
            if not i in hashmap:
                return False
            else:
                hashmap[i] -= 1
                if hashmap[i] < 0:
                    return False
        return True


# @lc code=end
