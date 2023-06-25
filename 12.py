def intToRoman(num) -> str:
    str1 = str(num)
    l1 = []
    dic1 = {"4": "IV", "9": "IX", "40": "XL", "90": "XC", "400": "CD", "900": "CM"}
    dic2 = {
        "1": "I",
        "5": "V",
        "10": "X",
        "50": "L",
        "100": "C",
        "500": "D",
        "1000": "M",
    }
    for i in range(len(str1)):
        digit = int(str1[i])
        l1.append(str(digit * (10 ** (len(str1) - 1 - i))))
    for i in range(len(l1)):
        if "4" in l1[i] or "9" in l1[i]:
            l1[i] = dic1[l1[i]]
        else:
            l1[i] = dic2[l1[i]]
    return "".join(l1)


num = 1994
intToRoman(num)
