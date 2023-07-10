#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.mDepth = 0
        self.depth = 0

    def traverse(self, tree):
        if not tree:
            return
        self.depth += 1
        self.mDepth = max(self.depth, self.mDepth)
        # front pos
        self.traverse(tree.left)
        self.traverse(tree.right)
        # back pos
        self.depth -= 1

    def maxDepth(self, root) -> int:
        self.traverse(root)
        return self.mDepth


# @lc code=end
