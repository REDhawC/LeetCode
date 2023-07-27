#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start


class Solution(object):
    def letterCombinations(self, digits):
        from collections import deque

        if not digits:
            return []
        charDict = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = deque()
        res = []
        idx = 0
        for i in charDict[int(digits[idx])]:
            queue.append(i)

        if len(digits) == 1:
            return queue

        print(queue)

        while queue:
            if idx + 1 == len(digits):
                return res

            size = len(queue)

            nextChars = charDict[int(digits[idx + 1])]
            for i in range(size):
                curChar = queue.popleft()
                for i in nextChars:
                    newCombination = curChar + i
                    queue.append(newCombination)
                    if len(newCombination) == len(digits):
                        res.append(newCombination)
            idx += 1
            # if idx + 1 == len(digits):
            #     return res
            # if idx + 1 == len(digits):
            for i in charDict[int(digits[idx])]:
                queue.append(i)

    # 2. DFS, backtrack


# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         # 注意边界条件
#         if not digits:
#             return []
#         # 一个映射表，第二个位置是"abc“,第三个位置是"def"。。。
#         # 这里也可以用map，用数组可以更节省点内存
#         d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#         # 最终输出结果的list
#         res = []

#         # 递归函数
#         def dfs(tmp, index):
#             # 递归的终止条件，注意这里的终止条件看上去跟动态演示图有些不同，主要是做了点优化
#             # 动态图中是每次截取字符串的一部分，"234"，变成"23"，再变成"3"，最后变成""，这样性能不佳
#             # 而用index记录每次遍历到字符串的位置，这样性能更好
#             if index == len(digits):
#                 res.append(tmp)
#                 return
#             # 获取index位置的字符，假设输入的字符是"234"
#             # 第一次递归时index为0所以c=2，第二次index为1所以c=3，第三次c=4
#             # subString每次都会生成新的字符串，而index则是取当前的一个字符，所以效率更高一点
#             c = digits[index]
#             # map_string的下表是从0开始一直到9， ord(c)-48 是获取c的ASCII码然后-48,48是0的ASCII
#             # 比如c=2时候，2-'0'，获取下标为2,letter_map[2]就是"abc"
#             letters = d[int(c)]
#             # change to int(c) , more easy-understanding

#             # 遍历字符串，比如第一次得到的是2，页就是遍历"abc"
#             for i in letters:
#                 # 调用下一层递归，用文字很难描述，请配合动态图理解
#                 dfs(tmp + i, index + 1)

#         dfs("", 0)
#         return res


# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         size = len(digits)
#         if size == 0:
#             return []
#         results = []
#         path = ""
#         charDict = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }

#         def backtrack(path, digit, charMap, used):
#             if len(path) == size:
#                 print(path)
#                 results.append(path)
#                 return

#             for charIdx in range(len(charMap[digit])):
#                 if not used[digit][charIdx]:
#                     used[digit][charIdx] = True
#                     path += charMap[digit][charIdx]
#                     digit += 1
#                     backtrack(path, digit, charMap, used)
#                     digit -= 1
#                     used[digit][charIdx] = False
#                     path = path[:-1]

#         used = []
#         charMap = []
#         for digit in digits:
#             charMap.append(charDict[digit])
#             used.append([False for _ in range(len(charDict[digit]))])

#         digit = 0
#         backtrack(path, digit, charMap, used)

#         return results


#         print(used)
#         print(charMap)
#         print(results)


# Solution.letterCombinations(Solution, "23")

# @lc code=end
