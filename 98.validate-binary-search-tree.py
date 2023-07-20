#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        nodes = []

        def traverse(root):
            nonlocal nodes
            if not root:
                return
            traverse(root.left)
            nodes.append(root.val)
            traverse(root.right)

        traverse(root)
        # print(nodes)
        for i in range(len(nodes) - 1):
            if nodes[i] >= nodes[i + 1]:
                return False
        return True


# @lc code=end
