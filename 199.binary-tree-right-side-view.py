#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        nodes = []

        def traverse(root):
            nonlocal nodes
            if not root:
                return
            print(root.val)
            nodes.append(root.val)
            if root.right:
                traverse(root.right)
            else:
                traverse(root.left)

            return root

        traverse(root)
        return nodes


# @lc code=end
