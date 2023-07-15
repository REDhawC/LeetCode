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


# class Solution:
#     def invertTree(self, root):
#         # 二叉树遍历函数
#         def traverse(root: TreeNode):
#             if not root:
#                 return

#             # 每一个节点需要做的事就是交换它的左右子节点
#             tmp = root.left
#             root.left = root.right
#             root.right = tmp

#             # 遍历框架，去遍历左右子树的节点
#             traverse(root.left)
#             traverse(root.right)

#         # 遍历二叉树，交换每个节点的子节点
#         traverse(root)
#         return root

# 1. traverse


# class Solution:
#     def invertTree(self, root):
#         def traverse(tree):
#             if not tree:
#                 return
#             # if tree.left and tree.right:
#             #     tree.left, tree.right = tree.right, tree.left
#             # if (tree.left and not tree.right) or (not tree.left and tree.right):
#             #     tree.left, tree.right = tree.right, tree.left
#             traverse(tree.left)
#             traverse(tree.right)
#             tree.left, tree.right = tree.right, tree.left

#         traverse(root)
#         return root


# 2. separate problem


class Solution:
    def invertTree(self, root):
        if not root:
            return

        left = self.invertTree(root.left)  # return left root
        right = self.invertTree(root.right)  # return right root
        # back pos: receive sons and swap
        root.left, root.right = right, left
        return root


# @lc code=end
