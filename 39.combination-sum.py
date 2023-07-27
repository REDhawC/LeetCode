#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(sumList):
            distance = target - sum(sumList)
            if distance == 0:
                #  不能使用sumList.sort()!!!!
                # 因为这修改了原list,等下回溯回去上一级需要list.pop(),导致顺序全乱了
                sorted_list = sorted(sumList)
                if sorted_list not in res:
                    # print("pass0:", sumList)
                    res.append(sorted_list)
                return
            for i in candidates:
                if i <= distance:
                    sumList.append(i)
                    backtrack(sumList)
                    sumList.pop()

        backtrack([])
        # print(res)
        return res


Solution.combinationSum(Solution, [7, 3, 2], 18)

# @lc code=end
