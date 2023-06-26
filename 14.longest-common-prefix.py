#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # 使用列表推导式创建多个数组
        new_arrays = [0] * len(strs)
        maxLen = 201
        for i in range(len(strs)):
            new_arrays[i] = strs[i]
            maxLen = min(maxLen, len(strs[i]))
        # print(maxLen)
        index = 0
        if maxLen > 0:
            flag = True
        else:
            return ans
        while flag and index < maxLen:
            currentLetter = new_arrays[0][index]
            for i in new_arrays:
                if i[index] != currentLetter:
                    flag = False
                    break
                currentLetter = i[index]
            if flag:
                ans += currentLetter
                index += 1
            else:
                return ans
        return ans


# @lc code=end
