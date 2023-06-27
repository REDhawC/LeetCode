class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                # 当递增至列尾 / 递减至列头时，
                # 需要反转flag来更改次序。
                flag = -flag
            i += flag
        return "".join(res)


print(Solution.convert(Solution, "PAYPALISHIRING", 3))
