#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class NodeList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        self.size += 1

    def removeMiddle(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLast(self):
        # when nodelist is empty:
        if self.size == 0:
            return None
        lastNode = self.tail.prev
        self.removeMiddle(lastNode)
        # no need to self.size -= 1,
        # cause we have done it in removeMiddle()
        return lastNode

    def getSize(self):
        return self.size


class LRUCache:
    def __init__(self, capacity):
        self.map = {}
        self.cache = NodeList()
        self.capacity = capacity

    def get(self, key):
        print("get:", key)
        if key in self.map:
            node = self.map[key]
            self.cache.removeMiddle(self.map[key])
            self.cache.addFirst(node)  # set node's prev and next
            self.map[key] = node
            return node.val
        else:
            return -1

    def put(self, key, val):
        print("put:", key, val)
        node = Node(key, val)
        if key in self.map:
            self.cache.removeMiddle(self.map[key])
            self.cache.addFirst(node)
            self.map[key] = node
        else:
            if self.cache.size == self.capacity:
                lastNode = self.cache.removeLast()
                self.map.pop(lastNode.key)
            self.cache.addFirst(node)
            self.map[key] = node


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
