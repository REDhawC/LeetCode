#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k: int):
        dummy = pre = fastPre = ListNode(next=head)
        fast = slow = pre.next
        length = 0
        while fast:
            fast = fast.next
            length += 1
        if length < 2 or k == 0:
            return head
        if k % length == 0:
            return head
        fast = pre.next
        for i in range(k % length):
            fast = fast.next
            fastPre = fastPre.next
        while fast != None:
            fast = fast.next
            slow = slow.next
            pre = pre.next
            fastPre = fastPre.next
        # print(slow.val, pre.val, fastPre.val, length)
        pre.next = None
        fastPre.next = head
        head = slow
        return head


# @lc code=end
