#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        import collections

        inDegree = [0] * numCourses
        neighborMap = {}
        for pair in prerequisites:
            inDegree[pair[0]] += 1
            if pair[1] not in neighborMap:
                neighborMap[pair[1]] = []
            neighborMap[pair[1]].append(pair[0])
        # print(inDegree, neighborMap)

        myDeque = collections.deque()
        res = []

        for index in range(len(inDegree)):
            if inDegree[index] == 0:
                myDeque.append(index)

        count = 0
        while len(myDeque) != 0:
            # print("md", myDeque)
            curCourse = myDeque.popleft()
            res.append(curCourse)
            count += 1
            successorList = neighborMap.get(curCourse)
            if successorList and len(successorList) != 0:
                nextEnqueue = []
                for i in successorList:
                    inDegree[i] -= 1
                    if inDegree[i] == 0:
                        nextEnqueue.append(i)
                # print(nextEnqueue)
                myDeque.extend(nextEnqueue)

        if count < numCourses:
            return []

        return res


# @lc code=end
