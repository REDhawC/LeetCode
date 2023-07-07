#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        head, curNode = None, None
        num = None
        while list1 or list2:
            if list1 == None:
                num = list2.val
                list2 = list2.next
            elif list2 == None:
                num = list1.val
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    num = list1.val
                    list1 = list1.next
                else:
                    num = list2.val
                    list2 = list2.next
            if not head:
                head = curNode = ListNode(num)
            else:
                curNode.next = ListNode(num)
                curNode = curNode.next
        return head


# @lc code=end
