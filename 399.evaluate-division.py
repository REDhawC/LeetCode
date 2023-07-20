#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

from collections import defaultdict

# @lc code=start
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        equationsSize = len(equations)
        # 第1步：预处理，将变量的值与id进行映射，使得并查集的底层使用数组实现，方便编码
        hashMap = {}
        id = 0
        for i in range(equationsSize):
            equation = equations[i]
            var1, var2 = equation[0], equation[1]

            if var1 not in hashMap:
                hashMap[var1] = id
                id += 1
            if var2 not in hashMap:
                hashMap[var2] = id
                id += 1

        unionFind = UnionFind(2 * equationsSize)
        for i in range(equationsSize):
            equation = equations[i]
            var1, var2 = equation[0], equation[1]
            id1, id2 = hashMap[var1], hashMap[var2]
            value = values[i]
            unionFind.union(id1, id2, value)

        # 第2步：做查询
        queriesSize = len(queries)
        res = []
        for i in range(queriesSize):
            query = queries[i]
            var1, var2 = query[0], query[1]
            id1, id2 = hashMap.get(var1), hashMap.get(var2)
            if id1 is None or id2 is None:
                res.append(-1.0)
            else:
                res.append(unionFind.isConnected(id1, id2))
        return res


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.weight = [1.0] * n

    def union(self, x: int, y: int, value: float) -> None:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        self.parent[rootX] = rootY
        self.weight[rootX] = self.weight[y] * value / self.weight[x]

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[origin]
        return self.parent[x]

    def isConnected(self, x: int, y: int) -> float:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return self.weight[x] / self.weight[y]
        else:
            return -1.0


# @lc code=end
