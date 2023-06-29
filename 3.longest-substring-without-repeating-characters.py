#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        subS = ""
        maxLen = 0
        if len(s) == 1:
            return 1
        while right < len(s):
            subS += s[right]
            maxLen = max(maxLen, right - left + 1)
            if right + 1 == len(s):
                return maxLen
            while s[right + 1] in subS:
                left += 1
                subS = subS[1:]
            right += 1
        return maxLen


l = "au"

Solution.lengthOfLongestSubstring(Solution, l)


# @lc code=end
