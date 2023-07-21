#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#


# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        import collections

        def BFS(queue, cur: int, newBoard):
            for i in range(1, 6 + 1):
                # print(cur + i)
                # print(queue)
                # 如果走到需要传送的位置，则传送
                if cur + i < len(newBoard) and newBoard[cur + i] != -1:
                    queue.append(newBoard[cur + i])
                else:
                    if cur + i < len(newBoard) and cur + i not in visited:
                        queue.append(cur + i)

        n = len(board)
        newBoard = [-1]
        rowIndex = 0
        for index in range(n - 1, -1, -1):
            rowIndex += 1
            if rowIndex % 2 == 0:
                temp = board[index]
                temp.reverse()
                newBoard.extend(temp)
            else:
                newBoard.extend(board[index])
        # print(newBoard[2])
        # 存储已经遍历过的位置
        visited = set()
        queue = collections.deque()
        ans = 0
        queue.append(1)
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                # print("cur:", cur)
                # print("vis:", visited)
                if cur == n * n:
                    return ans
                if cur not in visited:
                    BFS(queue, cur, newBoard)  # 扩展新状态
                    visited.add(cur)  # 将当前状态加入到已访问集合中
            ans += 1
        return -1


# @lc code=end
