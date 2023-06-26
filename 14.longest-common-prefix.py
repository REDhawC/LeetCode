#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         shortest = min(strs, key=len)
#         for index in range(len(shortest)):
#             current = shortest[index]
#             for word in strs:
#                 if index == len(word) or word[index] != current:
#                     return shortest[:index]
#         return shortest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index in range(len(strs[0])):
            # 把遍历第index个字母的index限定在第一个单词的长度内，
            # 如果你字母数=0，当然不进入循环；同时防止取第一个单词的current不成功
            wordId = 0
            current = strs[0][index]
            while wordId < len(strs):
                if index == len(strs[wordId]) or strs[wordId][index] != current:
                    # 如果字母不一致 or index达到当前单词的长度， 就结束
                    return strs[0][:index]
                wordId += 1
        return strs[0]
        # 如果不进入循环，字母数=0，就返回空的给它


# class Solution:
#     # 空间复杂度过高， 可以优化到O(1)!
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         ans = ""
#         # 使用列表推导式创建多个数组
#         new_arrays = [0] * len(strs)
#         maxLen = 201
#         for i in range(len(strs)):
#             new_arrays[i] = strs[i]
#             maxLen = min(maxLen, len(strs[i]))
#         # print(maxLen)
#         index = 0
#         if maxLen > 0:
#             flag = True
#         else:
#             return ans
#         while flag and index < maxLen:
#             currentLetter = new_arrays[0][index]
#             for i in new_arrays:
#                 if i[index] != currentLetter:
#                     flag = False
#                     break
#                 currentLetter = i[index]
#             if flag:
#                 ans += currentLetter
#                 index += 1
#             else:
#                 return ans
#         return ans


# @lc code=end
