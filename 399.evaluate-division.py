#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

from collections import defaultdict

# @lc code=start


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # 初始化一个字典类型的图
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v
        print(graph)

        def dfs(start, end):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1
            visited.add(start)
            for i in graph[start]:
                if end == i:
                    return graph[start][end]

                if i not in visited:
                    # this START's neighbor is not END,
                    # but we can dig it deeper cause END may be in his neighbors.
                    ans = dfs(i, end)
                    if ans != -1:
                        return graph[start][i] * ans
            return -1

        res = []
        for var1, var2 in queries:
            # set visited to empty every time to avoid infinite loop.
            visited = set()
            res.append(dfs(var1, var2))
        return res


# @lc code=end
