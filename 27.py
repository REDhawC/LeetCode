nums = [0, 1, 2, 2, 3, 0, 4, 2]


def removeElement(nums, val: int) -> int:
    count = 0
    lenNums = len(nums)
    while val in nums:
        count += 1
        nums.remove(val)
    return lenNums - count


removeElement(nums, 2)
print(nums)
