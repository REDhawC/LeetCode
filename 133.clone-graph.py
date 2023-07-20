#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        visited = {}

        def dfs(node):
            nonlocal visited
            if node in visited:
                return visited[node]

            newNode = Node(node.val)
            visited[node] = newNode
            for i in node.neighbors:
                newNode.neighbors.append(dfs(i))
            return newNode

        return dfs(node)


# @lc code=end
