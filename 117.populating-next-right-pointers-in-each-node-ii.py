#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        # cur可以看做是每一层的链表的头结点
        cur = root
        while cur:
            # 为了方便操作在下一层前面添加一个哑结点
            # pre表示访问下一层节点的前一个节点
            dummy = Node(0)
            pre = dummy
            # 遍历当前层的链表
            while cur:
                if cur.left:
                    # 如果当前节点的左子节点不为空，就让pre节点的next指向它，也就是把它串起来
                    pre.next = cur.left
                    # 然后再更新pre
                    pre = pre.next
                if cur.right:
                    # 同理参照左子树
                    pre.next = cur.right
                    pre = pre.next
                # 继续访问这一行的下一个节点
                cur = cur.next
            # 把下一层串联成一个链表之后，让它赋值给cur，后续继续循环，直到cur为空为止
            cur = dummy.next
        return root


# class Solution:
#     def connect(self, root: "Node") -> "Node":
#         def getValidNode(father):
#             if not father:
#                 return None
#             if father.left and father.right:
#                 return father.left
#             elif father.left:
#                 return father.left
#             elif father.right:
#                 return father.right

#         if not root:
#             return root
#         curLayer = root
#         while curLayer:
#             flag = 1
#             father = curLayer
#             stack = []
#             while father:
#                 curNode = getValidNode(father)
#                 if not curNode:
#                     father = father.next
#                 if flag and curNode:
#                     firstNode = curNode
#                     flag = 0
#                 while curNode:
#                     while not (father.left or father.right):
#                         if not father.next:
#                             break
#                         father = father.next
#                     if curNode == father.left and father.right:
#                         curNode.next = father.right
#                     else:
#                         curNode.next = getValidNode(father)
#                     curNode = curNode.next

#                 father = father.next
#             if flag:
#                 return root
#             curLayer = firstNode

#         return root


# @lc code=end
