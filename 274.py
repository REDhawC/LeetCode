l1 = [0]


def hIndex(citations) -> int:
    maxArt = len(citations)
    total = 0
    counter = [0] * (maxArt + 1)
    for i in citations:
        if i >= maxArt:
            counter[maxArt] += 1
        else:
            counter[i] += 1
    for i in range(7, -1, -1):
        print(i)
        # total += counter[i]
        # print(total)
        # if total >= i:
        #     return i


print(hIndex(l1))
