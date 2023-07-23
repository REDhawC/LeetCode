#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        from collections import deque

        queue = deque()

        queue.append(root)
        depth = 1
        while queue and root:
            size = len(queue)
            for idx in range(size):
                node = queue.popleft()
                if not node.left and not node.right:
                    # reach a leaf, return the result
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1
        return 0


# @lc code=end
