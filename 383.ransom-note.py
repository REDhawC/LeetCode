#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        # set up hashmap
        for i in magazine:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for i in ransomNote:
            if not i in hashmap:
                return False
            hashmap[i] -= 1
            if hashmap[i] < 0:
                # < 0 -> the magazine cannot fulfill requirements.
                return False
        return True


# @lc code=end
