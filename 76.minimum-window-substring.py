#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #
        def getMin(window, hashmap1, minLen):
            hashmap2 = {}
            flag = 1
            i = 0
            while i < len(window) and flag:
                curItem = window[i]
                if curItem not in hashmap2:
                    hashmap2[curItem] = 1
                else:
                    hashmap2[curItem] += 1
                i += 1
            for key in hashmap1:
                if not key in hashmap2:
                    flag = 0
                    return -1
                if key in hashmap2 and hashmap2[key] < hashmap1[key]:
                    flag = 0
            if flag:
                minLen = min(minLen, len(window))
                return minLen
            else:
                return -1

        #
        # left = 0
        right = 0
        hashmap1 = {}
        window = ""
        tLen = len(t)
        minLen = 10**5 + 1
        minStr = ""
        for i in t:
            if not i in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1
        while right < len(s):
            window += s[right]
            while getMin(window, hashmap1, minLen) != -1:
                # requirements fulfilled
                if minLen > getMin(window, hashmap1, minLen):
                    minLen = getMin(window, hashmap1, minLen)
                    minStr = window
                window = window[1:]
            right += 1
        return minStr


s = "cabwefgewcwaefgcf"
t = "cae"
Solution.minWindow(Solution, s, t)


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         #
#         def getMin(window, hashmap1, minLen):
#             hashmap2 = {}
#             flag = 1
#             i = 0
#             while i < len(window) and flag:
#                 curItem = window[i]
#                 if curItem not in hashmap2:
#                     hashmap2[curItem] = 1
#                 else:
#                     hashmap2[curItem] += 1
#                 i += 1
#             for key in hashmap1:
#                 if not key in hashmap2:
#                     flag = 0
#                     return -1
#                 if key in hashmap2 and hashmap2[key] < hashmap1[key]:
#                     flag = 0
#             if flag:
#                 minLen = min(minLen, len(window))
#                 return minLen
#             else:
#                 return -1

#         #
#         # left = 0
#         right = 0
#         hashmap1 = {}
#         window = ""
#         tLen = len(t)
#         minLen = 10**5 + 1
#         minStr = ""
#         for i in t:
#             if not i in hashmap1:
#                 hashmap1[i] = 1
#             else:
#                 hashmap1[i] += 1
#         while right < len(s):
#             window += s[right]
#             while len(window) >= tLen:
#                 if getMin(window, hashmap1, minLen) == -1:
#                     tempRight = right
#                     tempWindow = window
#                     while right < len(s) - 1 and getMin(window, hashmap1, minLen) == -1:
#                         right += 1
#                         window += s[right]
#                     if getMin(window, hashmap1, minLen) != -1 and minLen > getMin(
#                         window, hashmap1, minLen
#                     ):
#                         minLen = getMin(window, hashmap1, minLen)
#                         minStr = window
#                     window = tempWindow
#                     right = tempRight
#                 else:
#                     minLen = getMin(window, hashmap1, minLen)
#                     minStr = window
#                 window = window[1:]
#             right += 1
#         return minStr


# s = "a"
# t = "a"
# Solution.minWindow(Solution, s, t)

# @lc code=end
