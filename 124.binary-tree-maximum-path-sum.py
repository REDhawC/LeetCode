#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self) -> None:
    #     self.maxSum=-1001
    def maxPathSum(self, root):
        maxSum = float("-inf")

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0
            #
            leftMaxVal = dfs(root.left)
            rightMaxVal = dfs(root.right)
            # post pos
            # the max val including current root val, like a curve
            # use the root as a linking node, calculate the maxVal of this link.
            curMaxVal = root.val + leftMaxVal + rightMaxVal
            maxSum = max(maxSum, curMaxVal)
            # calculate current maxVal with the best Route
            # as for routes , we have 3 choices:
            # 0->pick neither ; left->pick left ; right->pick right
            outputMaxRouteVal = root.val + max(0, leftMaxVal, rightMaxVal)
            if outputMaxRouteVal < 0:
                return 0  # tell upper nodes that this route is banned
            else:
                return outputMaxRouteVal

        dfs(root)
        return maxSum


# @lc code=end
