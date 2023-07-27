#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        size = len(digits)
        if size == 0:
            return []
        results = []
        path = ""
        charDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(path, digit, charMap, used):
            if len(path) == size:
                print(path)
                results.append(path)
                return

            for charIdx in range(len(charMap[digit])):
                if not used[digit][charIdx]:
                    used[digit][charIdx] = True
                    path += charMap[digit][charIdx]
                    digit += 1
                    backtrack(path, digit, charMap, used)
                    digit -= 1
                    used[digit][charIdx] = False
                    path = path[:-1]

        used = []
        charMap = []
        for digit in digits:
            charMap.append(charDict[digit])
            used.append([False for _ in range(len(charDict[digit]))])

        for digit in range(len(digits)):
            backtrack(path, digit, charMap, used)
        print(used)
        print(charMap)
        print(results)


Solution.letterCombinations(Solution, "23")

# @lc code=end
