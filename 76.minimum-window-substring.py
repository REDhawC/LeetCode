#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections

        left = 0
        right = 0
        hashmap1 = collections.Counter(t)
        totalNeedNum = len(t)
        window = ""
        tLen = len(t)
        minLen = 10**5 + 1
        minStr = ""
        while right < len(s):
            window += s[right]
            curChar = s[right]
            if hashmap1[curChar] > 0:
                # this item is required
                totalNeedNum -= 1
            hashmap1[curChar] -= 1
            # we reduce 1 even the char didn't exist before
            if totalNeedNum == 0:
                # we got enough amount of all chars(but possibly exceeds)
                # the next step is to remove unnecessary LEFT chars
                while True:
                    curChar = s[left]
                    if hashmap1[curChar] == 0:
                        # 持续切去最左的不必要元素,直到遇到一个必须的元素,才终止
                        # id curChar is needed, stop removeing left items
                        break
                    # else, we can remove it
                    window = window[1:]
                    hashmap1[curChar] += 1
                    # after removeing it, the value increases 1,
                    # it is like the requirement +1
                    left += 1
                if len(window) < minLen:
                    # 去除多余元素后,比较,取最小
                    minLen = len(window)
                    minStr = window
                # 满足一个阶段+去重+取最小后,我们需要进一步,那么必须再舍弃一个最左
                # [即便是必要的item]
                hashmap1[s[left]] += 1
                window = window[1:]
                # 记得补偿一个totalNeedNum和hashmap里面+=1
                totalNeedNum += 1
                left += 1
            # 正常的right递增放在最后
            right += 1
        return minStr


s = "ADOBECODEBANC"
t = "ABC"

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
