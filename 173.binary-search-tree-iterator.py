#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root):
        self.nodes = []

        def traverse(root, nodes):
            if not root:
                return
            traverse(root.left, nodes)
            nodes.append(root)
            traverse(root.right, nodes)
            return root

        traverse(root, self.nodes)
        self.nodes_Index = 0
        self.length = len(self.nodes)
        for i in self.nodes:
            print(i.val)

    def next(self) -> int:
        self.nodes_Index += 1
        # if self.nodes_Index - 1 < self.length:
        #     return None
        print("next:", self.nodes[self.nodes_Index - 1].val)
        return self.nodes[self.nodes_Index - 1].val

    def hasNext(self) -> bool:
        nextIndex = self.nodes_Index + 1

        print("has:", nextIndex)
        if nextIndex <= self.length:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
