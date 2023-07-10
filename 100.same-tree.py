#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_leaves = []
        q_leaves = []

        def traverse(res, tree):
            if not tree:
                res.append(None)
                return

            res.append(tree.val)
            # front pos
            traverse(res, tree.left)
            traverse(res, tree.right)

            return res

        p_leaves = traverse(p_leaves, p)
        q_leaves = traverse(q_leaves, q)
        return p_leaves == q_leaves


# @lc code=end
