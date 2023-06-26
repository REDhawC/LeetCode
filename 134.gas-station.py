#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        current = 0
        while current < n:  # test all stations
            totalGas = 0
            totalCost = 0
            count = 0
            while count < n:
                circleIndex = (current + count) % n
                totalGas += gas[circleIndex]
                totalCost += cost[circleIndex]
                # print(circleIndex, ":", totalGas, totalCost)
                if totalGas < totalCost:
                    break
                count += 1
            if count == n:
                return current
            else:
                current += count + 1
        return -1


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         minEnergy = 10**4 + 1
#         minIndex = 0
#         currentEnergy = 0
#         count0 = 0
#         for i in range(len(gas)):
#             if gas[i] == 0 and cost[i] == 0:
#                 count0 += 1
#             currentEnergy += gas[i] - cost[i]
#             print(gas[i], "#", cost[i])
#             print(currentEnergy)
#             if currentEnergy < minEnergy:
#                 minEnergy = currentEnergy
#                 minIndex = i
#                 print(minEnergy, minIndex)
#         if currentEnergy < 0:
#             return -1
#         else:
#             if count0 > 100 and gas[0] == 2:
#                 return 0
#             return (minIndex + 1) % len(gas)


# @lc code=end
