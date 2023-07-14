#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
            # means this node has no left leaves

        # root is located at the first pos of preorder
        rootVal = preorder[preStart]
        # based on the hashmap, search for rootVal's index in inorder
        index = self.hashmap[rootVal]
        # as we all know, the indexes < root's index are the left leaves.
        leftSize = index - inStart

        root = TreeNode(rootVal)
        root.left = self.build(
            preorder, preStart + 1, preStart + leftSize, inorder, inStart, index - 1
        )
        root.right = self.build(
            preorder, preStart + leftSize + 1, preEnd, inorder, index + 1, inEnd
        )
        return root


# @lc code=end
