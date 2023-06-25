#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        dic1 = {}
        for i in range(len(citations) + 1):
            count = 0
            for k in citations:
                if k >= i:
                    count += 1
            if count >= i:
                dic1[i] = count
        return max(dic1.keys())


# @lc code=end
