#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        nodes = []

        def traverse(root):
            nonlocal nodes

            if not root:
                return
            #
            traverse(root.left)
            nodes.append(root.val)
            traverse(root.right)

            return root

        traverse(root)
        # print(nodes)
        return nodes[k - 1]


# @lc code=end
