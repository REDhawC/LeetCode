#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.preOrder = []

    def traverse(self, root):
        if not root:
            return
        self.preOrder.append(root)
        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)

    # 1. violent traverse

    # def flatten(self, root):
    #     self.traverse(root)
    #     for i in range(len(self.preOrder) - 1):
    #         self.preOrder[i].left = None
    #         self.preOrder[i].right = self.preOrder[i + 1]

    # 2.logic

    def flatten(self, root):
        while root:
            # pass when root has no left
            if not root.left:
                root = root.right
            else:
                pre = root.left
                while pre.right:
                    pre = pre.right
                print(pre.val)
                pre.right = root.right
                root.right = root.left
                root.left = None

                root = root.right

    """
    Do not return anything, modify root in-place instead.
    """


# @lc code=end
