#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        bonus = 0
        head, curNode = None, None
        while l1 or l2:
            if not l1:
                num1 = 0
            else:
                num1 = l1.val
            if not l2:
                num2 = 0
            else:
                num2 = l2.val
            sum = num1 + num2 + bonus
            print(sum)
            bonus = sum // 10
            if head == None:
                # initiate the new node-list
                head = curNode = ListNode(sum % 10)
            else:
                curNode.next = ListNode(sum % 10)
                curNode = curNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if bonus != 0:
            curNode.next = ListNode(bonus)
        return head


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         s1, s2 = "", ""
#         stack = []
#         nextNode = l1
#         while nextNode != None:
#             stack.append(nextNode.val)
#             nextNode = nextNode.next
#         while len(stack) != 0:
#             s1 += str(stack.pop())
#         stack = []
#         nextNode = l2
#         while nextNode != None:
#             stack.append(nextNode.val)
#             nextNode = nextNode.next
#         while len(stack) != 0:
#             s2 += str(stack.pop())
#         result = str(int(s1) + int(s2))
#         print(result)
#         firstNode = ListNode(int(result[-1]))
#         node = firstNode
#         for i in range(len(result) - 2, -1, -1):
#             node.next = ListNode(int(result[i]))
#             node = node.next
#         return firstNode


# @lc code=end
