def plusOne(digits):
    str = ""
    for i in range(len(digits)):
        str += str(digits[i])
    num1 = eval(str)
    num2 = num1 + 1
    for i in range(num2):
        digits[i] = eval(str(num2)[i])


plusOne([1, 2, 3])
