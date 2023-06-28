#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         res = []
#         if not nums or n < 3:
#             return []
#         nums.sort()
#         res = []
#         for i in range(n):
#             if nums[i] > 0:
#                 return res
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             L = i + 1
#             R = n - 1
#             while L < R:
#                 if nums[i] + nums[L] + nums[R] == 0:
#                     res.append([nums[i], nums[L], nums[R]])
#                     while L < R and nums[L] == nums[L + 1]:
#                         L = L + 1
#                     while L < R and nums[R] == nums[R - 1]:
#                         R = R - 1
#                     L = L + 1
#                     R = R - 1
#                 elif nums[i] + nums[L] + nums[R] > 0:
#                     R = R - 1
#                 else:
#                     L = L + 1
#         return res


class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        i = 0
        if len(nums) < 3:
            return []
        while i < len(nums) - 2:
            # we have 3 pointers here:
            # i , left , right
            curVal = nums[i]
            if curVal > 0:
                return ans
            left = i + 1
            right = len(nums) - 1
            if (nums[i] == nums[i - 1]) and i > 0:
                i += 1
                continue
            else:
                while left < right:
                    count = curVal + nums[left] + nums[right]
                    if count < 0:
                        left += 1
                    elif count > 0:
                        right -= 1

                    else:
                        sub = [nums[i], nums[left], nums[right]]
                        ans.append(sub)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
            i += 1
        # print(ans)
        return ans


pro = [1, -1, -1, 0]
Solution.threeSum(Solution, pro)

# @lc code=end
