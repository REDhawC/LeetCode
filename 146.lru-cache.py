#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key  # 节点的key
        self.val = val  # 节点的value
        self.next = next  # 指向后一个节点的指针
        self.prev = prev  # 指向前一个节点的指针


class DoubleList:
    def __init__(self):
        # self.head和self.tail都充当dummy节点（哨兵节点）
        self.head = Node(-1, -1)  # 头节点
        self.tail = Node(-1, -1)  # 尾节点
        self.head.next = self.tail  # 初始化，头节点指向尾节点
        self.tail.prev = self.head  # 初始化，尾节点指向头节点
        self.size = 0  # 链表大小

    def addFirst(self, x):
        """在最前面加个节点x,注意语句顺序, 很经典！"""
        x.next = self.head.next  # x的next指针指向头节点的下一个节点
        x.prev = self.head  # x的prev指针指向头节点
        self.head.next.prev = x  # 头节点的下一个节点的prev指针指向x
        self.head.next = x  # 头节点的next指针指向x
        self.size += 1  # 链表大小加1

    def remove(self, x):
        """删除节点x,调用这个函数说明x一定存在"""
        x.prev.next = x.next  # x的前一个节点的next指针指向x的下一个节点
        x.next.prev = x.prev  # x的下一个节点的prev指针指向x的前一个节点
        self.size -= 1  # 链表大小减1

    def removeLast(self):
        """
        删除链表中最后一个节点，并返回该节点
        注意双向链表的删除时间复杂度是O(1)的，因为立刻能找到该删除节点的前驱
        """
        if self.size == 0:
            return None
        last_node = self.tail.prev  # 获取尾节点的前一个节点，即链表中最后一个节点
        self.remove(last_node)  # 删除该节点
        return last_node  # 返回该节点

    def getSize(self):
        return self.size  # 返回链表大小


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # LRU Cache的容量
        self.map = {}  # 哈希表，用于快速定位key对应的节点
        self.cache = DoubleList()  # 双向链表，用于维续节点的访问顺序

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1  # 如果key不存在于LRU Cache中，则返回-1
        val = self.map[key].val  # 获取key对应的value值
        self.put(key, val)  # 将该节点移到链表头部
        return val  # 返回value值

    def put(self, key: int, value: int) -> None:
        new_item = Node(key, value)  # 新建一个节点
        if key in self.map:
            self.cache.remove(self.map[key])  # 如果key已存在于LRU Cache中，则将对应节点移到链表头部
            self.cache.addFirst(new_item)  # 将新节点添加到链表头部
            self.map[key] = new_item  # 更新map中的key-value对应关系
        else:
            if self.capacity == self.cache.getSize():
                last_node = self.cache.removeLast()  # 如果LRU Cache已满，则删除链表尾部的节点
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
