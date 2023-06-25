#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        count, farest = 0, 0
        end = 0  # 无论如何都必须从index 0 开始跳到另一个格子
        for i in range(len(nums) - 1):  # 不需要遍历到最后一位
            farest = max(farest, i + nums[i])
            if i == end:  # 当遍历到区间尾部的时候,说明需要跳了,
                # 根据贪心算法, 直接跳到目前确立的farest位置
                end = farest
                count += 1  # 跳跃次数+1
        return count

        # end, max_pos = 0, 0
        # steps = 0
        # for i in range(len(nums) - 1):
        #     max_pos = max(max_pos, nums[i] + i)
        #     if i == end:
        #         end = max_pos
        #         steps += 1
        # return steps


# @lc code=end
