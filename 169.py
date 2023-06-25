def majorityElement(nums) -> int:
    # nums.sort()
    # fast = 1
    # slow = 0
    # count = 1
    # while fast < len(nums):
    #     print(count)
    #     if nums[fast] != nums[slow]:
    #         if count > len(nums) / 2:
    #             break
    #         else:
    #             count = 1
    #     else:
    #         count += 1
    #     fast += 1
    #     slow += 1
    # return nums[slow]
    import collections

    counts = collections.Counter(nums)
    for i in counts:
        print(i, counts.get(i))
    print(counts)
    return max(counts.keys(), key=counts.get)


l1 = [3, 3, 4]
print(majorityElement(l1))
