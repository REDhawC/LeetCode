#
# @lc app=leetcode id=1601 lang=python3
#
# [1601] Maximum Number of Achievable Transfer Requests
#


# @lc code=start
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        delta = [0] * n
        ans, cnt, zero = 0, 0, n

        def dfs(pos: int) -> None:
            nonlocal ans, cnt, zero
            if pos == len(requests):
                if zero == n:
                    ans = max(ans, cnt)
                return

            # 不选 requests[pos]
            dfs(pos + 1)

            # 选 requests[pos]
            z = zero
            cnt += 1
            x, y = requests[pos]
            zero -= delta[x] == 0
            delta[x] -= 1
            zero += delta[x] == 0
            zero -= delta[y] == 0
            delta[y] += 1
            zero += delta[y] == 0
            dfs(pos + 1)
            delta[y] -= 1
            delta[x] += 1
            cnt -= 1
            zero = z

        dfs(0)
        return ans


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        buildingNetChange = [0] * n
        maxTransfer = -1
        path = []
        requestNum = len(requests)

        def backtracking(idx, trans, path, buildingStatus):
            nonlocal maxTransfer

            if idx == requestNum:
                if trans > maxTransfer:
                    if buildingStatus.count(0) == n:
                        # print(buildingStatus)
                        # print(path)
                        maxTransfer = max(maxTransfer, trans)

                return

            for i in range(idx, requestNum):
                # choose building[i]
                curRequest = requests[i]
                path.append(curRequest)
                buildingStatus[curRequest[0]] -= 1
                buildingStatus[curRequest[1]] += 1
                trans += 1
                backtracking(i + 1, trans, path, buildingStatus)
                path.pop()
                buildingStatus[curRequest[0]] += 1
                buildingStatus[curRequest[1]] -= 1
                trans -= 1
                backtracking(i + 1, trans, path, buildingStatus)

        backtracking(0, 0, path, buildingNetChange)
        return maxTransfer


# Solution.maximumRequests(Solution, 5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]])
# @lc code=end
