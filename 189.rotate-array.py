#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) - 1
        if k != 0:
            k = k % (n + 1) - 1  # cause 0 <= k <= 10^5
            self.reverse(nums, 0, n)
            # flip the whole list, but order reversed
            self.reverse(nums, 0, k)
            # filp k items in the front to recover the order
            self.reverse(nums, k + 1, n)
            # filp the remaining items

    def reverse(self, nums: List[int], left: int, right: int):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        """
        Do not return anything, modify nums in-place instead.
        """


# @lc code=end
