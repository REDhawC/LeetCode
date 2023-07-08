#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        if not head.next:
            return head.next
        dummy = pre = ListNode(next=head)
        slow = fast = head
        for i in range(n):
            # let fast move n steps forward
            fast = fast.next
        # when fast arrived the end,
        # the loop break and we have slow located at our target.
        while fast:
            pre = pre.next
            slow = slow.next
            fast = fast.next

        pre.next = slow.next
        return dummy.next


# @lc code=end
