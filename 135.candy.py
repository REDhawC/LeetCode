#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#


# @lc code=start


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         candies, left, right = (
#             [1] * len(ratings),
#             [1] * len(ratings),
#             [1] * len(ratings),
#         )
#         # fulfill principle1: if right > left,right=left+1
#         for i in range(1, len(ratings)):
#             if ratings[i - 1] < ratings[i]:
#                 left[i] = left[i - 1] + 1
#         # fulfill principle2: if left > right,left=right+1
#         for i in range(len(ratings) - 2, -1, -1):
#             if ratings[i] > ratings[i + 1]:
#                 right[i] = right[i + 1] + 1
#         for i in range(len(ratings)):
#             # get the max value of LEFT and RIGHT,
#             # so we can fulfill all principles at the same time.
#             candies[i] = max(left[i], right[i])
#         print(left, right, candies)
#         return sum(candies)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ascending = 0
        descending = 0
        candies = [1] * len(ratings)

        # 第一遍扫描，处理降序和等值情况
        for i, rating in enumerate(ratings):
            if i > 0:  # 避开第一个，从第二个开始才判断
                if rating > ratings[i - 1]:
                    ascending += 1
                    descending = 0
                    candies[i] = candies[i - 1] + 1
                elif rating == ratings[i - 1]:
                    ascending = 0
                    descending = 0
                else:
                    descending += 1
                    ascending = 0
                    candies[i - descending] = max(
                        candies[i - descending], descending + 1
                    )
            print(i, ":", rating, "##", candies)

        # 第二遍扫描，处理升序情况
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# @lc code=end
