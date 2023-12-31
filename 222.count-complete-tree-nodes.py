#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root) -> int:
        sum = 0

        def traverse(root):
            nonlocal sum
            if not root:
                return
            sum += 1
            traverse(root.left)
            traverse(root.right)
            return root

        traverse(root)
        return sum


# @lc code=end
