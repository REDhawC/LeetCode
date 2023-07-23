#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        def plusOne(pwdStr, pos):
            oldChar = pwdStr[pos]
            if oldChar == "9":
                newChar = "0"
            else:
                newChar = str(int(oldChar) + 1)
            return pwdStr[:pos] + newChar + pwdStr[pos + 1 :]

        def minusOne(pwdStr, pos):
            oldChar = pwdStr[pos]
            if oldChar == "0":
                newChar = "9"
            else:
                newChar = str(int(oldChar) - 1)
            return pwdStr[:pos] + newChar + pwdStr[pos + 1 :]

        deadSet = set(deadends)
        queue = deque()
        visited = set()
        step = 0
        queue.append("0000")
        while queue:
            size = len(queue)
            for i in range(size):
                curNum = queue.popleft()
                if curNum == target:
                    return step
                if curNum in deadSet:
                    # continue to avoid deadNums BEING ADDED to the queue
                    continue
                if curNum not in visited:
                    visited.add(curNum)
                    # add 8 directions to the queue
                    for i in range(4):
                        queue.append(plusOne(curNum, i))
                        queue.append(minusOne(curNum, i))
            step += 1
        return -1


# @lc code=end
