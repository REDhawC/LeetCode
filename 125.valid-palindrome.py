#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # the two pointers are legal and ready
            if s[left].isalnum() and s[right].isalnum():
                if s[left].isalpha() and s[right].isalpha():
                    if s[left].lower() != s[right].lower():
                        return False
                else:
                    if s[left] != s[right]:
                        return False
                left += 1
                right -= 1
            # if any one of the pointers is illegal,
            # the other one must wait.
            elif not s[left].isalnum() and s[right].isalnum():
                left += 1
            elif s[left].isalnum() and not s[right].isalnum():
                right -= 1
            else:
                # both are illegal characters -> pass
                left += 1
                right -= 1
        return True

        # index = 0
        # stack = []
        # newS = ""
        # while index < len(s):
        #     if s[index].isalnum():
        #         if s[index].isalpha():
        #             item = s[index].lower()
        #         else:
        #             item = s[index]
        #         stack.append(item)
        #         newS += item
        #     index += 1

        # convertedStr = ""
        # for i in range(len(stack)):
        #     convertedStr += stack.pop()
        # if convertedStr == newS:
        #     return True


ss = "A man, a plan, a canal: Panama"

Solution.isPalindrome(Solution, ss)

# @lc code=end
