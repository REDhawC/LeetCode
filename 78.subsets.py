#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    # 2.answer (must choose one number, but which one?)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        res = []
        path = []

        def backtrack(path, idx):
            res.append(path.copy())
            if idx == length:
                return

            # loop current numList and choose
            for i in range(idx, length):
                path.append(nums[i])
                backtrack(path, i + 1)  # add 1 to prevent duplication
                path.pop()

        backtrack(path, 0)
        return res

    # 1. input perspective ( choose or not? )

    def subsets(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        res = []
        path = []

        def backtrack(path, idx):
            if idx == length:
                res.append(path.copy())
                return

            # input the num
            path.append(nums[idx])
            backtrack(path, idx + 1)
            path.pop()

            # refuse to input the num
            backtrack(path, idx + 1)

        backtrack(path, 0)
        return res


# @lc code=end
