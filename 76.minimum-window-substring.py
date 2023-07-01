#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start


class Solution:
    # my own version! cool!!
    def minWindow(self, s: str, t: str) -> str:
        import collections

        hashmap = collections.Counter(t)
        window = ""
        left, right = 0, 0
        minLen = 10**5 + 1
        minStr = ""
        necessaryNum = len(t)
        while right < len(s):
            window += s[right]
            curChar = s[right]
            if hashmap[curChar] > 0:
                necessaryNum -= 1
            hashmap[curChar] -= 1
            if necessaryNum == 0:
                while hashmap[window[0]] != 0:
                    hashmap[window[0]] += 1
                    window = window[1:]
                    left += 1
                if len(window) < minLen:
                    minLen = len(window)
                    minStr = window
                hashmap[window[0]] += 1
                left += 1
                window = window[1:]
                necessaryNum += 1
            right += 1
        return minStr


s = "ADOBECODEBANC"
t = "ABC"

Solution.minWindow(Solution, s, t)

# @lc code=end
