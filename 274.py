l1 = [1, 3, 1]


def hIndex(citations) -> int:
    dic1 = {}
    for i in range(len(citations) + 1):
        count = 0
        for k in citations:
            if k >= i:
                count += 1
        if count >= i:
            dic1[i] = count
    return max(dic1.keys())


print(hIndex(l1))
