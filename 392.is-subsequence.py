#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            # 如果匹配成功，i就可以往下移动，
            # 否则就只有j指针能移动，直到再遇到I为止。
            if s[i] == t[j]:
                i += 1
            j += 1
        # 如果i指针能遍历到最后，说明j指针能全部满足，
        # 即结果为True, 否则为False
        return i == n


ss = "abc"
tt = "ahbgdc"
Solution.isSubsequence(Solution, ss, tt)
# @lc code=end
