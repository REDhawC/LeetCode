#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        def traverse(tree):
            if not tree:
                return
            if tree.left and tree.right:
                tree.left, tree.right = tree.right, tree.left
            if (tree.left and not tree.right) or (not tree.left and tree.right):
                tree.left, tree.right = tree.right, tree.left
            traverse(tree.left)
            traverse(tree.right)

        traverse(root)
        return root


# @lc code=end
