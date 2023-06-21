nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
nums = nums[-k:] + nums[0 : k + 1]
print(nums)
