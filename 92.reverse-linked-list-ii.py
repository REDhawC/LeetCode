#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        p0 = dummy = ListNode(next=head)
        # set dummy to avoid
        for i in range(left - 1):
            # locate at the node in front of the to-be-reversed part
            p0 = p0.next

        pre = None
        curNode = p0.next
        for i in range(right - left + 1):
            former_next = curNode.next
            curNode.next = pre
            pre = curNode
            curNode = former_next

        p0.next.next = curNode
        # the former starting left node's next was set to be None
        # now we make it -> curNode [the node behind the reversed part]
        p0.next = pre
        # the node in front of the to-be-reversed part should point to
        # the new starting node

        return dummy.next


# @lc code=end
