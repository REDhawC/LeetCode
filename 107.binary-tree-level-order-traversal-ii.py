#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        queue = deque()
        visited = set()
        resQueue = deque()

        queue.append(root)
        while queue:
            size = len(queue)
            tempList = list()
            for idx in range(size):
                curNode = queue.popleft()
                if curNode not in visited:
                    visited.add(curNode)
                    if curNode.left:
                        queue.append(curNode.left)
                    if curNode.right:
                        queue.append(curNode.right)
                    tempList.append(curNode.val)
            # print(tempList)
            resQueue.appendleft(tempList)
        return resQueue


# @lc code=end
