#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        length = 0
        lenNode = head
        # calculate the length of the node-list
        while lenNode:
            length += 1
            lenNode = lenNode.next
        p0 = dummy = ListNode(next=head)
        # set dummy to avoid
        while length >= k:
            # if the remaining length is not enough for reversing,
            # break and return
            pre = None
            curNode = p0.next
            for i in range(k):
                print(i)
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

            length -= k
            # update the remaining length.
            if length < k:
                # if the remaining length is not enough for reversing,
                # break and return
                return dummy.next

            for i in range(k):
                # keep marching to the node in front of the to-be-reversed part
                p0 = p0.next


# @lc code=end
