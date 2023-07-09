#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x: int):
        lessQueue = []
        equalOrMoreQueue = []
        node = head
        length = 0
        while node:
            if node.val < x:
                lessQueue.append(node)
            else:
                equalOrMoreQueue.append(node)
            length += 1
            node = node.next
        if length < 2:
            return head
        if len(lessQueue) > 0:
            for i in range(len(lessQueue) - 1):
                lessQueue[i].next = lessQueue[i + 1]
                print(lessQueue[i].val)
            if len(equalOrMoreQueue) > 0:
                lessQueue[-1].next = equalOrMoreQueue[0]

        if len(equalOrMoreQueue) > 0:
            for i in range(len(equalOrMoreQueue) - 1):
                equalOrMoreQueue[i].next = equalOrMoreQueue[i + 1]
                print(equalOrMoreQueue[i].val)
            equalOrMoreQueue[-1].next = None
        if len(lessQueue) > 0:
            head = lessQueue[0]
        else:
            head = equalOrMoreQueue[0]
        return head


# @lc code=end
