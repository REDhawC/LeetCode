#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
        self.hashmap = {}

    def buildTree(self, inorder, postorder):
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i

        # build
        def build(inorder, inStart, inEnd, postorder, postStart, postEnd):
            if postStart > postEnd:
                return None
            rootVal = postorder[postEnd]
            # 每次遍历实际上就只是取postEnd的值来生成root
            # +
            # 利用rootVal在inorder里面的index来进行切割
            inorder_Index = self.hashmap[rootVal]
            leftSize = inorder_Index - inStart
            root = TreeNode(rootVal)
            # recursion to build left and right
            root.left = build(
                inorder,
                inStart,
                inorder_Index - 1,
                postorder,
                postStart,
                postStart + leftSize - 1,
            )

            root.right = build(
                inorder,
                inorder_Index + 1,
                inEnd,
                postorder,
                postStart + leftSize,
                postEnd - 1,
            )

            return root

        return build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

        # quickly use val to get -> index in INORDER


# @lc code=end
