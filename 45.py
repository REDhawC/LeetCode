nums = [2, 3, 1, 1, 4]
# nums = [1, 1, 1, 1, 1]


def jump(nums) -> int:
    count, farest = 0, 0
    end = 0  # 无论如何都必须从index 0 开始跳到另一个格子
    for i in range(len(nums) - 1):  # 不需要遍历到最后一位
        farest = max(farest, i + nums[i])
        print(i, "#", farest)
        if i == end:
            print("old end:", end)  # 当遍历到区间尾部的时候,说明需要跳了,
            # 根据贪心算法, 直接跳到目前确立的farest位置
            end = farest
            print("new end:", end)
            count += 1  # 跳跃次数+1
    return count
    # if len(nums) - 1 == 0:
    #     return 0
    # if nums[0] >= len(nums) - 1:
    #     return 1
    # current = 0
    # minCount = 0
    # farest = 0
    # while current < len(nums) - 1:
    #     minCount += 1
    #     for i in range(current, current + nums[current]):
    #         farest = max(farest, i + nums[i])
    #         print(i, "#", farest)
    #         if farest >= len(nums) - 1:
    #             return minCount
    #     print("done")
    #     current = farest
    # return 0

    # count, farest = 0, 0
    # end = 0
    # for i in range(len(nums) - 1):
    #     farest = max(farest, i + nums[i])
    #     print(i, "#", farest)
    #     if i == end:
    #         print("done")
    #         end = farest
    #         count += 1
    # return count


print(jump(nums))
