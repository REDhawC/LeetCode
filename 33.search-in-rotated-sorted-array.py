#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = -1
        right = len(nums)
        firstNum = nums[0]
        if firstNum == target:
            return 0
        while left + 1 < right:
            mid = (left + right) // 2
            # list all the blues
            if nums[mid] < firstNum:
                if target < firstNum:
                    if nums[mid] > target:
                        right = mid
                    elif nums[mid] < target:
                        left = mid
                    else:
                        return mid
                else:
                    right = mid
            else:  # nums[mid] > firstNum
                if target > firstNum:
                    if nums[mid] > target:
                        right = mid
                    elif nums[mid] < target:
                        left = mid
                    else:
                        return mid
                else:  # target < firstNum
                    left = mid

        if left == len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1


# Solution.search(Solution, [1, 3, 5], 1)


# @lc code=end
