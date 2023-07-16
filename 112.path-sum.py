#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.sum = 0
        self.targetSum = 0
        self.ans = False
        self.dummy = None

    def traverse(self, root):
        if not root:
            return
        # front pos
        self.sum += root.val
        if self.sum == self.targetSum and not (root.left or root.right):
            self.ans = True
        self.traverse(root.left)
        self.traverse(root.right)
        # back pos
        self.sum -= root.val
        return root

    def hasPathSum(self, root, targetSum: int) -> bool:
        self.targetSum = targetSum
        self.traverse(root)
        return self.ans


# @lc code=end
