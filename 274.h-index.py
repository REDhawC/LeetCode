#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxArt = len(citations)
        total = 0
        counter = [0] * (maxArt + 1)
        for i in citations:
            if i >= maxArt:
                # 超出文章数量的引用数,直接记为文章总数
                counter[maxArt] += 1
            else:
                counter[i] += 1
        for i in range(maxArt, -1, -1):
            # 从后往前一一校对
            total += counter[i]
            # 如果累计文献数>=当前要求引用量,
            # 即符合Hindex要求
            if total >= i:
                return i

        # dic1 = {}
        # for i in range(len(citations) + 1):
        #     count = 0
        #     for k in citations:
        #         if k >= i:
        #             count += 1
        #     if count >= i:
        #         dic1[i] = count
        # return max(dic1.keys())


# @lc code=end
