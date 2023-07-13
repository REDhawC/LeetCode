#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
        self.nodesLeft = list()
        self.nodesRight = list()

    def isSymmetric(self, root) -> bool:
        def traverseLeft(tree):
            if not tree:
                self.nodesLeft.append(None)
                return
            self.nodesLeft.append(tree.val)
            # front pos
            traverseLeft(tree.left)
            traverseLeft(tree.right)

        def traverseRight(tree):
            if not tree:
                self.nodesRight.append(None)
                return
            self.nodesRight.append(tree.val)
            # front pos
            traverseRight(tree.right)
            traverseRight(tree.left)

        traverseLeft(root.left)
        traverseRight(root.right)
        print(self.nodesLeft, self.nodesRight)

        return self.nodesLeft == self.nodesRight


# @lc code=end
