#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        import collections

        myDeque = collections.deque()
        myDeque.append(root)
        res = list()
        level = 0

        while myDeque:
            size = len(myDeque)
            for i in range(size):
                # this "size" is the size of upper layer
                curNode = myDeque.popleft()
                # calculate the avg of upper layer
                if i == 0:
                    res.append(0)
                # print("before:", res[level])
                res[level] = (res[level] * i + curNode.val) / (i + 1)
                # print("after:", res[level])

                # make prep for the lower layer
                if curNode.left:
                    myDeque.append(curNode.left)
                if curNode.right:
                    myDeque.append(curNode.right)

                if i == size - 1:
                    level += 1

        return res


# @lc code=end
