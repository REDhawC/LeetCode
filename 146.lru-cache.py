#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.val = val
        self.key = key
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeNum = 0
        self.head = None

    def get(self, key: int) -> int:
        node = self.head
        while node:
            if node.key == key:
                newNode = ListNode(node.key, node.val, self.head)
                self.head = newNode
                return node.val
            node = node.next
        return -1

    def put(self, key: int, value: int) -> None:
        if self.nodeNum < self.capacity:
            node = ListNode(key, value, self.head)
            self.head = node
            self.nodeNum += 1
        else:
            count = 0
            pre = ListNode(next=self.head)
            node = self.head
            tempKey = [-1] * 2
            while node:
                if node.key != tempKey[0]:
                    count += 1
                if count == self.capacity:
                    pre.next = None
                    print("pre:", (pre.key, pre.val))
                    if self.capacity == 1:
                        self.head = None
                    break
                tempKey[0] = node.key
                tempKey[1] = node.val
                node = node.next
                pre = pre.next
            node = ListNode(key, value, self.head)
            self.head = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)

# obj.put(1, 1)
# obj.put(2, 2)
# obj.get(1)
# obj.put(3, 3)
# node = obj.head
# while node:
#     print(node.key)
#     node = node.next
# @lc code=end
