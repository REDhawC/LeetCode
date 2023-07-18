#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        import collections

        if not root:
            return []
        myDeque = collections.deque()
        myDeque.append(root)

        level = 0
        res = []
        while myDeque:
            size = len(myDeque)
            for i in range(size):
                curFather = myDeque.popleft()
                if i == 0:
                    res.append([])
                res[level].append(curFather.val)
                # append the next layer nodes
                if curFather.left:
                    myDeque.append(curFather.left)
                if curFather.right:
                    myDeque.append(curFather.right)
                if i == size - 1:
                    level += 1
        return res


# @lc code=end
