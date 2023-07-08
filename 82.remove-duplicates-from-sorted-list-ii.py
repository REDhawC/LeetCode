#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(next=head)
        curNode = pre.next
        while curNode:
            if curNode.next:
                if curNode.val == curNode.next.val:
                    while curNode.val == curNode.next.val:
                        curNode = curNode.next
                        if not curNode.next:
                            break
                    pre.next = curNode.next
                    curNode = curNode.next
                else:
                    pre = pre.next
                    curNode = curNode.next
            else:
                pre = pre.next
                curNode = curNode.next

        return dummy.next


# @lc code=end
