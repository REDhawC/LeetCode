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

    def addFirst(self, x):
        """插入在 head 和 tail 之间, 总共需要梳理4个箭头!"""
        x.next = self.head.next  # x的next指针指向头节点的下一个节点
        x.prev = self.head  # x的prev指针指向头节点
        self.head.next.prev = x  # 头节点的下一个节点的prev指针指向x
        self.head.next = x  # 头节点的next指针指向x
        self.size += 1  # 链表大小加1

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
    def __init__(self, capacity: int):
        self.capacity = capacity  # LRU Cache的容量
        self.map = {}  # 哈希表，用于快速定位key对应的节点,补足了双向链表查找缓慢的特点!
        self.cache = DoubleList()  # 双向链表，用于维续节点的访问顺序

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
            self.cache.remove(self.map[key])  # 如果key已存在于LRU Cache中，则将对应节点删除,
            self.cache.addFirst(new_item)  # 然后将key相同的新节点添加到链表头部 -> 进行更新
            self.map[key] = new_item  # 更新map中的key-value对应关系
        else:
            if self.capacity == self.cache.getSize():
                last_node = (
                    self.cache.removeLast()
                )  # 如果LRU Cache已满，则用removeLast删除链表尾部的节点
                self.map.pop(last_node.key)  # 删除map中对应的key-value对应关系
            self.cache.addFirst(new_item)  # 将新节点添加到链表头部
            self.map[key] = new_item  # 更新map中的key-value对应关系


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
