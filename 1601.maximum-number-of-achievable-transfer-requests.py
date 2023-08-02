#
# @lc app=leetcode id=1601 lang=python3
#
# [1601] Maximum Number of Achievable Transfer Requests
#


# @lc code=start
# class Solution:
#     def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
#         delta = [0] * n
#         ans, cnt, zero = 0, 0, n

#         def dfs(pos: int) -> None:
#             nonlocal ans, cnt, zero
#             if pos == len(requests):
#                 if zero == n:
#                     ans = max(ans, cnt)
#                 return

#             # 不选 requests[pos]
#             dfs(pos + 1)

#             # 选 requests[pos]
#             z = zero
#             cnt += 1
#             x, y = requests[pos]
#             zero -= delta[x] == 0
#             delta[x] -= 1
#             zero += delta[x] == 0
#             zero -= delta[y] == 0
#             delta[y] += 1
#             zero += delta[y] == 0
#             dfs(pos + 1)
#             delta[y] -= 1
#             delta[x] += 1
#             cnt -= 1
#             zero = z

#         dfs(0)
#         return ans


# class Solution:
#     def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
#         buildingNetChange = [0] * n
#         maxTransfer = -1
#         zeroBuildingNum = n
#         requestNum = len(requests)

#         def backtracking(idx, trans):
#             nonlocal maxTransfer, buildingNetChange, zeroBuildingNum

#             if idx == requestNum:
#                 if trans > maxTransfer:
#                     if zeroBuildingNum == n:
#                         maxTransfer = max(maxTransfer, trans)
#                 return

#             curRequest = requests[idx]
#             if buildingNetChange[curRequest[0]] == 0:
#                 zeroBuildingNum -= 1
#             if buildingNetChange[curRequest[1]] == 0 and curRequest[0] != curRequest[1]:
#                 zeroBuildingNum -= 1

#             buildingNetChange[curRequest[0]] -= 1
#             buildingNetChange[curRequest[1]] += 1

#             if buildingNetChange[curRequest[0]] == 0:
#                 zeroBuildingNum += 1
#             if buildingNetChange[curRequest[1]] == 0 and curRequest[0] != curRequest[1]:
#                 zeroBuildingNum += 1

#             trans += 1
#             backtracking(idx + 1, trans)
#             # path.pop()

#             if buildingNetChange[curRequest[0]] == 0:
#                 zeroBuildingNum -= 1
#             if buildingNetChange[curRequest[1]] == 0 and curRequest[0] != curRequest[1]:
#                 zeroBuildingNum -= 1

#             buildingNetChange[curRequest[0]] += 1
#             buildingNetChange[curRequest[1]] -= 1

#             if buildingNetChange[curRequest[0]] == 0:
#                 zeroBuildingNum += 1
#             if buildingNetChange[curRequest[1]] == 0 and curRequest[0] != curRequest[1]:
#                 zeroBuildingNum += 1

#             trans -= 1

#             backtracking(idx + 1, trans)

#         backtracking(0, 0)
#         return maxTransfer


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        buildingNetChange = [0] * n
        maxTransfer = -1
        zeroBuildingNum = n
        requestNum = len(requests)

        def backtracking(idx, trans):
            nonlocal maxTransfer, buildingNetChange, zeroBuildingNum

            if idx == requestNum:
                if trans > maxTransfer:
                    if zeroBuildingNum == n:
                        maxTransfer = max(maxTransfer, trans)
                return

            b1, b2 = requests[idx]

            if b1 != b2:
                tempZero = zeroBuildingNum

                zeroBuildingNum -= buildingNetChange[b1] == 0
                # offset the original status:
                # if the status is already 0, we might overly +1;
                # if the status is already not 0, this line do nothing;

                buildingNetChange[b1] -= 1  # update the new building 1 status
                zeroBuildingNum += buildingNetChange[b1] == 0
                # if == 0 , zeroNum+1; else, do nothing
                zeroBuildingNum -= buildingNetChange[b2] == 0
                # offset the original status again
                buildingNetChange[b2] += 1
                zeroBuildingNum += buildingNetChange[b2] == 0
            trans += 1
            backtracking(idx + 1, trans)
            if b1 != b2:
                buildingNetChange[b1] += 1
                buildingNetChange[b2] -= 1
                zeroBuildingNum = tempZero
            trans -= 1

            backtracking(idx + 1, trans)

        backtracking(0, 0)
        return maxTransfer


# class Solution:
#     def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
#         buildingNetChange = [0] * n
#         maxTransfer = -1
#         path = []
#         zeroBuildingNum = n
#         requestNum = len(requests)

#         def backtracking(idx, trans, path):
#             nonlocal maxTransfer, buildingNetChange, zeroBuildingNum

#             if idx == requestNum:
#                 if trans > maxTransfer:
#                     if zeroBuildingNum == n:
#                         print("pass", buildingNetChange)
#                         print("pass", path)
#                         maxTransfer = max(maxTransfer, trans)

#                 return

#             for i in range(idx, requestNum):
#                 # choose building[i]

#                 curRequest = requests[i]
#                 path.append(curRequest)
#                 buildingNetChange[curRequest[0]] -= 1
#                 buildingNetChange[curRequest[1]] += 1
#                 if buildingNetChange[curRequest[0]] == 0:
#                     zeroBuildingNum += 1
#                 if buildingNetChange[curRequest[1]] == 0:
#                     zeroBuildingNum += 1
#                 if buildingNetChange[curRequest[0]] != 0:
#                     zeroBuildingNum -= 1
#                 if buildingNetChange[curRequest[1]] != 0:
#                     zeroBuildingNum -= 1
#                 trans += 1
#                 # print("in:", buildingNetChange)
#                 # print("in:", path)
#                 # print("in:", zeroBuildingNum, trans)
#                 backtracking(i + 1, trans, path)
#                 path.pop()
#                 buildingNetChange[curRequest[0]] += 1
#                 buildingNetChange[curRequest[1]] -= 1
#                 if buildingNetChange[curRequest[0]] == 0:
#                     zeroBuildingNum += 1
#                 if buildingNetChange[curRequest[1]] == 0:
#                     zeroBuildingNum += 1
#                 if buildingNetChange[curRequest[0]] != 0:
#                     zeroBuildingNum -= 1
#                 if buildingNetChange[curRequest[1]] != 0:
#                     zeroBuildingNum -= 1
#                 trans -= 1
#                 # print("out:", buildingNetChange)
#                 # print("out:", path)
#                 # print("out:", zeroBuildingNum, trans)
#                 backtracking(i + 1, trans, path)

#         backtracking(0, 0, path)
#         return maxTransfer


Solution.maximumRequests(
    Solution, 3, [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]
)
# @lc code=end
