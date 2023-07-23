#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#


# @lc code=start
class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        import copy
        from collections import deque

        def swap(board, idx, newIdx):
            newBoard = copy.deepcopy(board)
            newBoard[idx], newBoard[newIdx] = newBoard[newIdx], newBoard[idx]
            return newBoard

        queue = deque()
        visited = set()
        target = tuple([1, 2, 3, 4, 5, 0])
        board[0].extend(board[1])
        board = board[0]
        # print(board)
        queue.append(tuple(board))
        step = 0
        possibleDirections = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        while queue:
            size = len(queue)
            # print(step)
            for i in range(size):
                curBoard = queue.popleft()
                if curBoard == target:
                    # print("tg:", curBoard)
                    return step
                if curBoard not in visited:
                    visited.add(tuple(curBoard))
                    _0_idx = list(curBoard).index(0)
                    for direction in possibleDirections[_0_idx]:
                        temp = swap(list(curBoard), _0_idx, direction)
                        # print(temp)
                        queue.append(tuple(temp))
            step += 1
        return -1


# @lc code=end
