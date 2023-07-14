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
        self.leaves = []

    def preOrderTraverse(self, tree):
        leaves = []
        if not tree:
            return leaves
        leaves.append(tree.val)
        # front pos
        leaves.extend(self.preOrderTraverse(tree.left))
        leaves.extend(self.preOrderTraverse(tree.right))
        return leaves
        # back pos

    # def traverse(self, tree):
    #     if not tree:
    #         return
    #     self.depth += 1
    #     self.mDepth = max(self.depth, self.mDepth)
    #     # front pos
    #     self.traverse(tree.left)
    #     self.traverse(tree.right)
    #     # back pos
    #     self.depth -= 1

    # 2. seperate problem
    def maxDepth(self, root):
        print(self.preOrderTraverse(root))

        return 0
        # back pos

    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     leftDepth = self.maxDepth(root.left)
    #     rightDepth = self.maxDepth(root.right)
    #     # when come out from left and right,
    #     # current maxDepth should + 1 ,
    #     # cause current node adds 1 to the depth.
    #     res = max(leftDepth, rightDepth) + 1
    #     return res

    # 1. traverse

    # def maxDepth(self, root) -> int:
    #     self.traverse(root)
    #     return self.mDepth


# @lc code=end
