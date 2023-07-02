#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_s = {}
        sStr = ""
        hashmap_t = {}
        tStr = ""
        # set up hashmap
        curInt = 0
        for index in range(len(s)):
            curChar = s[index]
            intStr = str(curInt)
            if not curChar in hashmap_s:
                curInt += 1
                intStr = str(curInt)
                hashmap_s[curChar] = intStr
            sStr += hashmap_s[curChar]

        curInt = 0
        for index in range(len(t)):
            curChar = t[index]
            intStr = str(curInt)
            if not curChar in hashmap_t:
                curInt += 1
                intStr = str(curInt)
                hashmap_t[curChar] = intStr
            tStr += hashmap_t[curChar]
        print(sStr, tStr, hashmap_s, hashmap_t)
        if sStr != tStr:
            return False
        else:
            return True


s = "egg"
t = "add"
Solution.isIsomorphic(Solution, s, t)


# @lc code=end
