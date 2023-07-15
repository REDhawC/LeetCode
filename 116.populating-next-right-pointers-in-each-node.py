#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# # 1. iteration

# class Solution:
#     def connect(self, root):
#         if not root:
#             return root
#         layer = root
#         while layer.left:  # traverse vertically
#             father = layer
#             while father:  # traverse within layer [horizontal]
#                 father.left.next = father.right
#                 if father.next:
#                     # tackle right nodes
#                     father.right.next = father.next.left
#                 father = father.next
#             layer = layer.left

#         return root

# 2. recursion


class Solution:
    def connect(self, root):
        if not root:
            return root
        # front pos:
        left = root.left
        right = root.right
        while left:
            # left leaf goes right,right leaf goes left.
            # this strategy can reach those nodes of different father and connect them.
            left.next = right
            left = left.right
            right = right.left

        # recursion: go to the next layer
        self.connect(root.left)
        self.connect(root.right)

        return root


# @lc code=end
