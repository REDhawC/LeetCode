#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # amazing sorting skill!
        # sort the intervals basing on the first value of each interval
        sortFunc = lambda x: x[0]
        intervals.sort(key=sortFunc)
        index = 0
        while index < len(intervals) - 1:
            if intervals[index][1] >= intervals[index + 1][0]:
                intervals[index][0] = min(intervals[index][0], intervals[index + 1][0])
                intervals[index][1] = max(intervals[index][1], intervals[index + 1][1])
                del intervals[index + 1]
                # rearrange the index to ensure loop all items
                index -= 1
            index += 1
        print(intervals)
        return intervals


m = [[1, 4], [0, 2], [3, 5]]
Solution.merge(Solution, m)

# @lc code=end
