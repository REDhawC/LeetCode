#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#


# @lc code=start


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         ascending = 0
#         descending = 0
#         candies = [1] * len(ratings)

#         # 第一遍扫描，处理降序和等值情况
#         for i, rating in enumerate(ratings):
#             if i > 0:
#                 if rating > ratings[i - 1]:
#                     ascending += 1
#                     descending = 0
#                     candies[i] = candies[i - 1] + 1
#                 elif rating == ratings[i - 1]:
#                     ascending = 0
#                     descending = 0
#                 else:
#                     descending += 1
#                     ascending = 0
#                     candies[i - descending] = max(
#                         candies[i - descending], descending + 1
#                     )

#         # 第二遍扫描，处理升序情况
#         for i in range(len(ratings) - 2, -1, -1):
#             if ratings[i] > ratings[i + 1]:
#                 candies[i] = max(candies[i], candies[i + 1] + 1)

#         return sum(candies)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        current = 1
        asc = 0
        dec = 0
        candy = [1] * len(ratings)
        while current < len(ratings):
            if ratings[current - 1] > ratings[current]:  # dec
                dec += 1
                if asc:
                    asc = 0
                    dec -= 1
                else:
                    candy[current - dec] = max(candy[current - dec], dec + 1)
            elif ratings[current - 1] == ratings[current]:  # equal
                dec, asc = 0, 0
            else:  # asc
                asc += 1
                candy[current] += asc
                if dec:
                    dec = 0
            current += 1
        current = 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)


# @lc code=end
