#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc code=start
class MinStack:
    def __init__(self):
        self.data = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.data) != 0:
            return self.data[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.data) != 0:
            return self.minStack[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
# @lc code=end
