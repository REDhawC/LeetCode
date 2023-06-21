#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    # 优点在于没有新添加变量来保存数组,空间复杂度为O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        # 1. add a [0] in the front
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] != 10:
                # save time if digits didn't increase
                break
            else:
                digits[i - 1] += 1
                digits[i] = 0
        if digits[0] == 0:
            # if digits didn't increase,
            # remove the first [0]
            return digits[1:]
        else:
            return digits

        """
    former solution
    """
        # def plusOne(self, digits: List[int]) -> List[int]:
        #     s = ""
        #     for i in range(len(digits)):
        #         s += str(digits[i])
        #     num1 = eval(s)
        #     num2 = num1 + 1
        #     for i in range(len(str(num2)) - 1):
        #         digits[i] = eval(str(num2)[i])
        #     if len(str(num2)) > len(str(num1)):
        #         digits.append(eval(str(num2)[-1]))
        #     else:
        #         digits[-1] = eval(str(num2)[-1])
        #     return digits


# @lc code=end
