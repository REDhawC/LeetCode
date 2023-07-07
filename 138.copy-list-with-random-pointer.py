#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#


# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return head
        hashmap = {}
        newNode = None
        oldNode = head
        while oldNode:
            # create new node for each old node,
            # and link them up in the hashmap.
            newNode = Node(oldNode.val)
            hashmap[oldNode] = newNode
            oldNode = oldNode.next

        oldNode = head
        while oldNode:
            # according to the old nodes' random and next,
            # we can use them as key to find the corresbonding NEW random or next node.
            if oldNode.next:
                hashmap[oldNode].next = hashmap[oldNode.next]
            if oldNode.random:
                hashmap[oldNode].random = hashmap[oldNode.random]
            oldNode = oldNode.next

        return hashmap[head]


# @lc code=end
