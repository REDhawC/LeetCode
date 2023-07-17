#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.sumStr = ""
        self.sum = 0

    def traverse(self, root):
        if not root:
            return
        self.sumStr += str(root.val)
        if not (root.left or root.right):
            self.sum += int(self.sumStr)
        #
        self.traverse(root.left)
        self.traverse(root.right)
        #
        self.sumStr = self.sumStr[:-1]
        return root

    def sumNumbers(self, root) -> int:
        self.traverse(root)
        return self.sum


# @lc code=end
