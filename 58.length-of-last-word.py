#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if i != len(s) - 1:
                if s[i + 1] != " " and s[i] == " ":
                    break
            if s[i] == " ":
                continue
            count += 1
        return count


# @lc code=end
