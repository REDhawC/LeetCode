#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        import collections

        if not root:
            return []
        myDeque = collections.deque()
        myDeque.append(root)
        res = []
        level = 0
        while myDeque:
            size = len(myDeque)
            for i in range(size):
                curFather = myDeque.popleft()
                # print(curFather.val)
                if i == 0:
                    res.append([])
                # if level % 2 == 0:
                #     curFather = myDeque.popleft()
                # else:
                #     curFather = myDeque.pop()
                res[level].append(curFather.val)
                if curFather.left:
                    myDeque.append(curFather.left)
                if curFather.right:
                    myDeque.append(curFather.right)
                if i == size - 1:
                    if level % 2 != 0:
                        res[level].reverse()
                    level += 1
        return res


# @lc code=end
