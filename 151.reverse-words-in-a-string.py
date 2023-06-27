#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        fast, slow = len(s) - 1, len(s) - 1
        if len(s) == 1:
            return s
        while fast > 0:
            fast -= 1
            if s[fast] != " " and s[fast + 1] == " ":
                # encounter new word
                slow = fast
                if fast == 0:
                    word = s[fast : slow + 1]
                    stack.append(word)
                    # print("1", word)
            elif s[fast] == " " and s[fast + 1] != " ":
                # reach the end of the word
                word = s[fast + 1 : slow + 1]
                stack.append(word)
                slow = fast + 1
                # print("2", word)
            elif s[fast] != " " and fast == 0:
                word = s[fast : slow + 1]
                stack.append(word)
                # print("3", word)
                # slow = fast + 1
        return " ".join(stack)


# Solution.reverseWords(Solution, "F R  I   E    N     D      S      ")


# @lc code=end
