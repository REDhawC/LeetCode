nums = [1, 1, 1, 2, 2, 3]


def removeDuplicates(nums) -> int:
    dic1 = {}
    for i in nums:
        if i in dic1.keys():
            dic1[i] += 1
        else:
            dic1[i] = 1
    for k in dic1:
        while dic1[k] > 2:
            nums.remove(k)
            dic1[k] -= 1
    return len(nums)


removeDuplicates(nums)
print(nums)
