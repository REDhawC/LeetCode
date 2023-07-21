#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        hashmap = {}
        for pair in prerequisites:
            inDegree[pair[0]] += 1
            if pair[1] in hashmap:
                hashmap[pair[1]].append(pair[0])
            else:
                hashmap[pair[1]] = []
                hashmap[pair[1]].append(pair[0])
        print(inDegree, hashmap)
        stack = []
        for index in range(len(inDegree)):
            if inDegree[index] == 0:
                stack.append(index)
        print(stack)

        count = 0
        while len(stack) > 0:
            curCourse = stack.pop()
            count += 1
            successorsList = hashmap.get(curCourse)
            if successorsList and len(successorsList) > 0:
                for i in successorsList:
                    inDegree[i] -= 1
                    if inDegree[i] == 0:
                        stack.append(i)
        return count == numCourses

    # def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    #     import collections

    #     graph = collections.defaultdict(list)
    #     marked = set()
    #     for a, b in prerequisites:
    #         graph[a].append(b)
    #         if a not in marked:
    #             marked.add(a)
    #         if b not in marked:
    #             marked.add(b)
    #         if len(marked) > numCourses or a == b:
    #             return False

    #     # for i in graph:
    #     #     print(i, ":", graph[i])

    #     def dfs(courses):
    #         nonlocal flag
    #         # print("dfs:", courses)
    #         for course in courses:
    #             # print(course, "main:", main)
    #             if course not in visited:
    #                 visited.add(course)
    #                 if course == main:
    #                     flag = False
    #                     return False
    #                 if course in graph:
    #                     dfs(graph[course])
    #         return True

    #     flag = True
    #     for i in graph:
    #         visited = set()
    #         main = i
    #         # print(i, "graph", graph[i])
    #         dfs(graph[i])
    #         if not flag:
    #             return flag
    #     return flag


# @lc code=end
