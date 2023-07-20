#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        import collections

        res = []  # 初始化结果列表
        if not root:
            return res  # 如果根节点为空，直接返回结果列表

        queue = collections.deque()  # 初始化队列
        queue.append(root)  # 将根节点加入队列中

        while queue:  # 当队列非空时循环
            size = len(queue)
            print(size)  # 获取当前队列中元素的个数，即当前层的节点个数
            for i in range(size):  # 遍历当前层的所有节点
                node = queue.popleft()  # 取出队列中的头节点
                if node.left:  # 如果头节点有左子节点，将左子节点加入队列中
                    queue.append(node.left)
                if node.right:  # 如果头节点有右子节点，将右子节点加入队列中
                    queue.append(node.right)
                if i == size - 1:  # 如果当前节点是当前层的最后一个节点，将其加入结果列表中
                    res.append(node.val)

        return res  # 返回结果列表

    # def rightSideView(self, root):
    #     nodes = []
    #     level = 0

    #     def traverse(root):
    #         nonlocal nodes, level
    #         if not root:
    #             return
    #         # print(root.val)
    #         level += 1
    #         if level > len(nodes):
    #             nodes.append(root.val)
    #         #
    #         traverse(root.right)
    #         traverse(root.left)
    #         #
    #         level -= 1
    #         return root

    #     traverse(root)
    #     for i in nodes:
    #         print(i)
    #     return nodes


# @lc code=end
