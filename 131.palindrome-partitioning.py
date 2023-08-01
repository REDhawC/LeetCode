#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        length = len(s)

        def isValid(s):
            fast = 0
            slow = len(s) - 1
            while fast <= slow:
                if s[fast] != s[slow]:
                    return False
                fast += 1
                slow -= 1
            return True

        def backtrack(idx):
            if idx == length:
                res.append(path.copy())
                return

            for i in range(idx, length):
                newStr = s[idx : i + 1]
                if isValid(newStr):
                    path.append(newStr)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res


# class Solution:
#     def partition(self, s: str) -> list[list[str]]:
#         res = []
#         visited = set()

#         # if len(s) == 1:
#         #     res.append([s])
#         #     return res

#         def isValid(s):
#             fast = 0
#             slow = len(s) - 1
#             while fast <= slow:
#                 if s[fast] != s[slow]:
#                     return False
#                 fast += 1
#                 slow -= 1
#             return True

#         def backtrack(s, subStrs):
#             # print(subStrs, "test")
#             if subStrs:
#                 flag = 1
#                 for sub in subStrs:
#                     if not isValid(sub):
#                         flag = 0
#                 if flag:
#                     # print(subStrs, "pass")
#                     newSubTuple = tuple(subStrs)
#                     visited.add(newSubTuple)
#                     res.append(subStrs)

#             for subIdx in range(len(subStrs)):
#                 sub = subStrs[subIdx]
#                 for idx in range(len(sub)):
#                     if idx == 0:
#                         newSubStrs = (
#                             subStrs[:subIdx] + [sub[idx:]] + subStrs[subIdx + 1 :]
#                         )
#                     else:
#                         newSubStrs = (
#                             subStrs[:subIdx]
#                             + [sub[:idx]]
#                             + [sub[idx:]]
#                             + subStrs[subIdx + 1 :]
#                         )
#                     newSubTuple = tuple(newSubStrs)
#                     if newSubTuple not in visited:
#                         # print("cutted:", subIdx, idx, newSubStrs)

#                         visited.add(newSubTuple)
#                         backtrack(s, newSubStrs)
#                         # visited.remove(newSubTuple)

#         backtrack(s, [s])

#         return res


Solution.partition(Solution, "abb")

# @lc code=end
