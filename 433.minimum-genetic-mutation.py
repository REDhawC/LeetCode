#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#


# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        import collections

        if endGene not in bank:
            return -1

        bank_Set = set(bank)  # set-> O(1) searching; better than list!
        queue = collections.deque()
        visited = set()
        queue.append([startGene, 0])
        while queue:
            node = queue.popleft()
            step = node[1]
            if node[0] == endGene:
                print(node[0], step)
                return step
            for i in range(len(node[0])):
                for char in ["A", "C", "G", "T"]:
                    newNode = node[0][:i] + char + node[0][i + 1 :]
                    if newNode == node[0]:
                        continue
                    if newNode not in bank_Set:
                        continue
                    if newNode not in visited:
                        visited.add(newNode)
                        print(newNode)
                        queue.append([newNode, step + 1])
        return -1


# @lc code=end
