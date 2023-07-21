#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#


# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if endGene not in bank:
            return -1

        def getDiffNums(gene1, gene2):
            res = [0, []]
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    res[0] += 1
                    res[1].append(i)
            return res

        print(getDiffNums(startGene, endGene))


# @lc code=end
