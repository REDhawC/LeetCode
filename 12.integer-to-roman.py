#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        dic = {  # 从小到大排列,符合贪心规则
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        for key in dic:  # 遍历哈希表, dic -> hashmap
            if num // key > 0:  # 如果当前的数字大于目前key,
                ans += dic[key] * (num // key)  # 添加对应个数的目前最大罗马数字
                num = num % key  # 取余数,进入下一轮循环
        return ans


# @lc code=end
