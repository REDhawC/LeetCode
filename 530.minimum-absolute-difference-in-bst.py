#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root) -> int:
        nodes = []
        minDiff = 10**5 + 1

        def traverse(root):
            nonlocal nodes

            if not root:
                return
            traverse(root.left)
            #
            nodes.append(root.val)
            #
            traverse(root.right)
            return root

        traverse(root)

        for i in range(len(nodes) - 1):
            diff = nodes[i + 1] - nodes[i]
            minDiff = min(diff, minDiff)
        return minDiff


# @lc code=end
