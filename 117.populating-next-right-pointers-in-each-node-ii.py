#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        def getValidNode(father):
            if not father:
                return None
            if father.left and father.right:
                return father.left
            elif father.left and not father.right:
                return father.left
            elif not father.left and father.right:
                return father.right

        if not root:
            return root
        curLayer = root
        while curLayer:
            print(1)
            flag = 1
            father = curLayer
            stack = []
            while father:
                print(2)
                curNode = getValidNode(father)
                # test valid father-nodes

                if not curNode:
                    father = father.next
                if flag and curNode:  # mark first son-node for layer deepening
                    firstNode = curNode
                    flag = 0
                # enter the layer looping
                while curNode:
                    print("val:", curNode.val)
                    print(3)
                    while not (father.left or father.right):
                        print(4)
                        if not father:
                            break
                        father = father.next
                    if curNode == father.left and father.right:
                        curNode.next = father.right
                    else:
                        curNode.next = getValidNode(father)
                    curNode = curNode.next

                father = father.next
            if firstNode:
                curLayer = firstNode
            else:
                return root


# @lc code=end
