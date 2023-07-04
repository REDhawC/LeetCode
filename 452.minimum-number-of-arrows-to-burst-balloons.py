#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrows = 1
        temp = points[0]
        for i in range(1, len(points)):
            if points[i][0] > temp[1]:
                arrows += 1
                temp = points[i]
            else:
                temp[0] = max(temp[0], points[i][0])
                temp[1] = min(temp[1], points[i][1])
        return arrows


# class Solution:
#     def findMinArrowShots(self, points: list[list[int]]) -> int:
#         sort_Func = lambda x: x[0]
#         points.sort(key=sort_Func)
#         print(points, len(points))
#         arrows = 0
#         index = 0
#         if len(points) == 1:
#             return 1
#         while index < len(points) - 1:
#             if points[index + 1][0] <= points[index][1]:
#                 temp = points[index]
#                 while index < len(points) - 1 and points[index + 1][0] <= temp[1]:
#                     temp = [
#                         max(temp[0], points[index][0]),
#                         min(temp[1], points[index][1]),
#                     ]
#                     index += 1
#                 arrows += 1
#                 index += 1
#             else:
#                 arrows += 1
#                 index += 1
#             if index == len(points) - 1:
#                 arrows += 1
#         return arrows


s = [
    [77171087, 133597895],
    [45117276, 135064454],
    [80695788, 90089372],
    [91705403, 110208054],
    [52392754, 127005153],
    [53999932, 118094992],
    [11549676, 55543044],
    [43947739, 128157751],
    [55636226, 105334812],
    [69348094, 125645633],
]
Solution.findMinArrowShots(Solution, s)


# @lc code=end
