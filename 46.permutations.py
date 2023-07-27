#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        result = []
        used = [False] * len(nums)
        length = len(nums)

        def backtrack(result, nums):
            if len(result) == length:
                # print(result)
                results.append(result.copy())
                return

            for option in range(len(nums)):
                if used[option]:
                    continue
                result.append(nums[option])
                used[option] = True
                #
                backtrack(result, nums)
                #
                used[option] = False
                result.pop()

        backtrack(result, nums)

        return results


n1 = [1, 2, 3]
Solution.permute(Solution, n1)

# @lc code=end
