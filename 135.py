def candy(ratings) -> int:
    ascending = 0
    descending = 0
    candies = [1] * len(ratings)

    # 第一遍扫描，处理从左往右，如果右>左，右=左+1
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
                candies[i - descending] = max(candies[i - descending], descending + 1)
        print(i, ":", rating, "##", candies)

    # 第二遍扫描，处理从右往左：左>右的规则
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        print(i, ":", ratings[i], "##", candies)
    return sum(candies)


rt = [1, 2, 87, 3, 2, 4]
candy(rt)
