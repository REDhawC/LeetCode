#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        index = 0
        ans = []
        if len(intervals) == 0:
            ans.append(newInterval)
            return ans
        while index < len(intervals):
            while index < len(intervals) and newInterval[0] > intervals[index][1]:
                # tail not in NEW interval
                ans.append(intervals[index])
                index += 1
            while index < len(intervals) and intervals[index][0] <= newInterval[1]:
                # tail in NEW interval and head <= NEW interval's tail
                newInterval[0] = min(newInterval[0], intervals[index][0])
                newInterval[1] = max(newInterval[1], intervals[index][1])
                index += 1
            ans.append(newInterval)
            while index < len(intervals) and intervals[index][0] > newInterval[1]:
                ans.append(intervals[index])
                index += 1
        print(ans)
        return ans


# class Solution:
#     def insert(
#         self, intervals: list[list[int]], newInterval: list[int]
#     ) -> list[list[int]]:
#         index = 0
#         if len(intervals) == 0:
#             intervals.append(newInterval)
#             return intervals
#         while index < len(intervals):
#             count = 0
#             if not (
#                 newInterval[0] <= intervals[index][1]
#                 and intervals[index][0] <= newInterval[1]
#             ):
#                 if newInterval[1] < intervals[index][0]:
#                     intervals.insert(index, newInterval)
#                     return intervals
#                 if index == len(intervals) - 1:
#                     if newInterval[0] < intervals[index][0]:
#                         intervals.insert(index, newInterval)
#                     else:
#                         intervals.insert(index + 1, newInterval)
#                     return intervals

#             while (
#                 newInterval[0] <= intervals[index][1]
#                 and intervals[index][0] <= newInterval[1]
#             ):
#                 count += 1
#                 newStart = min(intervals[index][0], newInterval[0])
#                 newEnd = max(intervals[index][1], newInterval[1])
#                 intervals[index], newInterval = [newStart, newEnd], [newStart, newEnd]
#                 if count > 1:
#                     del intervals[index - 1]
#                     index -= 1
#                 index += 1
#                 if index >= len(intervals) or newInterval[1] < intervals[index][0]:
#                     return intervals
#             index += 1
#         print(intervals)
#         return intervals


s = [[2, 4], [5, 7], [8, 10], [11, 13]]
m = [3, 6]
Solution.insert(Solution, s, m)


# @lc code=end
