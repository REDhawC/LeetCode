#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        if head:
            fast, slow = head.next, head
            while fast and fast.next:
                if fast == slow:
                    return True
                fast = fast.next.next
                slow = slow.next
        return False


# class Solution:
#     def hasCycle(self, head) -> bool:
#         hashmap = []
#         if head:
#             nextNode = head.next
#         else:
#             return False
#         while nextNode:
#             if nextNode in hashmap:
#                 return True
#             hashmap.append(nextNode)
#             nextNode = nextNode.next
#         return False


# @lc code=end
