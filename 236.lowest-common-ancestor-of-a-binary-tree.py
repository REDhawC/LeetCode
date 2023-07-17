#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         # 如果根节点为空，返回空
#         if not root:
#             return None
#         # 如果根节点为p或q，直接返回根节点
#         if root == p or root == q:
#             return root

#         # 在左子树中查找p和q的最近公共祖先
#         left = self.lowestCommonAncestor(root.left, p, q)
#         # 在右子树中查找p和q的最近公共祖先
#         right = self.lowestCommonAncestor(root.right, p, q)

#         print("root:", root.val, "left:", left.val, "right:", right.val)

#         # 如果左子树没有找到p和q的最近公共祖先，则直接返回右子树的结果
#         if not left:
#             return right
#         # 如果右子树没有找到p和q的最近公共祖先，则直接返回左子树的结果
#         if not right:
#             return left
#         # 如果p和q分别在当前节点的左子树和右子树中，则当前节点就是它们的最近公共祖先
#         if left and right:
#             print(left.val, right.val)
#             return root

#         # 如果无法找到p和q的最近公共祖先，则返回空
#         return None


# -------------------------
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        level = 1
        maxLevel = 0
        LCA = None

        def traverse(root):
            nonlocal level, maxLevel, LCA
            count = 0
            if not root:
                return count
            level += 1

            print(root.val)
            if root.val == q.val:
                count = 1
            if root.val == p.val:
                count = 2

            print(root.val, "count:", count)
            #
            left = traverse(root.left)
            right = traverse(root.right)
            #
            level -= 1
            print(root.val, "L:", left, "R:", right, count)
            if left + right + count == 3:
                # print("good", root.val, "level:", level)
                # print("L:", left, "R:", right)
                if level > maxLevel:
                    LCA = root
                    maxLevel = level

            # 下面这一步要想清楚,之前踩坑了!~~
            # 把该节点是否有left,right符合 以及 该节点是否符合一并返回.
            # 否则会丢失子节点的left/right
            return count + left + right

        traverse(root)
        return LCA


# -------------------------

# def traverse(root):
#     nonlocal level, maxLevel, LCA
#     count = 0
#     if not root:
#         return count
#     level += 1

#     # print(root.val)
#     left_count = traverse(root.left)
#     right_count = traverse(root.right)
#     level -= 1
#     # 后序一样可以判断当前root的数值,不是只有前序才可以哈哈哈

#     if root.val == q.val:
#         count = 1
#     if root.val == p.val:
#         count = 2

#     # print(root.val, "count:", count)
#     if left_count + right_count + count == 3:
#         # print("good", root.val, "level:", level)
#         if level > maxLevel[0]:
#             LCA[0] = root
#             maxLevel[0] = level

#     return left_count + right_count + count

# traverse(root)
# return LCA[0]


# @lc code=end
