#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        slow = 0
        fast = 0
        while fast < len(haystack):
            if haystack[fast] == needle[0]:
                slow = fast + len(needle)
                if slow > len(haystack):
                    return -1
                if haystack[fast:slow] == needle:
                    return fast
            fast += 1
        return -1


# @lc code=end
